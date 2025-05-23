from health_needs import get_required_tags
import math

def haversine_distance(coord1, coord2):
    R = 6371  # Earth radius in kilometers
    lat1, lon1 = coord1["lat"], coord1["lng"]
    lat2, lon2 = coord2["lat"], coord2["lng"]

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c, 2)

def score_facility(facility, need_value, user_location, weight_match=0.5, weight_safety=0.3, weight_distance=0.2):
    """Calculate how well a facility matches a user need"""
    required_tags = get_required_tags(need_value)
    facility_tags = facility.get("services", [])

    # Count how many tags match
    matched_tags = [tag for tag in required_tags if tag in facility_tags]
    match_score = len(matched_tags) / len(required_tags) if required_tags else 0

    raw_safety = facility.get("safety_score", 0)
    normalized_safety = raw_safety / 10

    distance_km = haversine_distance(user_location, facility["location"])
    distance_score = max(0, 1 - distance_km / 10)

    final_score = round(
        (match_score * weight_match) +
        (normalized_safety * weight_safety) +
        (distance_score * weight_distance), 3)

    return {
        "name": facility.get("name"),
        "match_score": round(match_score, 2),
        "safety_score": raw_safety,
        "distance_km": distance_km,
        "final_score": final_score,
        "matched_tags": matched_tags,
        "location": facility.get("location"),
        "all_services": facility_tags,
    }

def rank_facilities(facilities, need_value, user_location):
    """Return facilities sorted by how well they match the user's need"""
    scored = [score_facility(f, need_value, user_location) for f in facilities]
    return sorted(scored, key=lambda x: x["final_score"], reverse=True)

# Test script
if __name__ == "__main__":
    import json
    from health_needs import USER_HEALTH_NEEDS

    with open("facilities.json") as f:
        facilities = json.load(f)

    print("\nAvailable health needs:")
    for need in USER_HEALTH_NEEDS:
        print(f"- {need['label']} ({need['value']})")

    user_need = input("\nEnter the value of your health need (e.g. 'reproductive'): ").strip().lower()
    valid_values = [n["value"] for n in USER_HEALTH_NEEDS]

    if user_need not in valid_values:
        print("Invalid health need. Please run the program again and choose from the options.")
        exit()

    use_custom_location = input("Do you want to enter your current location? (y/n): ").strip().lower()
    if use_custom_location == "y":
        try:
            lat = float(input("Enter your latitude: "))
            lng = float(input("Enter your longitude: "))
            user_location = {"lat": lat, "lng": lng}
        except ValueError:
            print("Invalid coordinates. Using default location.")
            user_location = {"lat": -1.29, "lng": 36.82}
    else:
        user_location = {"lat": -1.29, "lng": 36.82}  # Default location (Nairobi)

    ranked = rank_facilities(facilities, user_need, user_location)

    print(f"\nTop facilities for: {user_need.upper()}\n")
    for f in ranked:
        print(f"{f['name']} - Score: {f['final_score']} | Distance: {f['distance_km']} km | Safety: {f['safety_score']}/10 | Matched: {f['matched_tags']}")
