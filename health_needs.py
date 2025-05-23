# Health needs & Service tags
USER_HEALTH_NEEDS = [
  {
    "label": "Maternity and Delivery",
    "value": "maternity",
    "required_tags": ["maternity", "delivery", "obgyn", "labor"]
  },
  {
    "label": "Reproductive Health / OB-GYN Visits",
    "value": "reproductive",
    "required_tags": ["gynecology", "family_planning", "fertility", "obgyn"]
  },
  {
    "label": "Pediatric Services",
    "value": "pediatrics",
    "required_tags": ["pediatrics", "child_health", "vaccination"]
  },
  {
    "label": "Sexual Health",
    "value": "sexual",
    "required_tags": ["contraceptives", "family_planning"]

  },
  {
    "label": "Emergency Sexual Health",
    "value": "emergency",
    "required_tags": ["rape","sexual_assault", "STI", "HIV" ]
  }
]

# Retrieve matching tags for a user need
def get_required_tags(need_value):
  for need in USER_HEALTH_NEEDS:
    if need["value"] == need_value:
      return need["required_tags"]
      return []

# Check if facility matches the user's selected health need
def facility_matches_need(facility, need_value):
  required_tags = get_required_tags(need_value)
  return any(tags in facility.get("services" ,[]) for tags in required_tags)

# Test
if __name__ == "__main__":
  sample_facility = {
    "name": "Hope Health Clicic",
    "services": ["maternity", "obgyn", "pediatrics", "STI", "family_planning"],
    "lat": -1.2921,
    "lng": 36.8219,
    "safety_score": 8.5
  }

  user_selected_need = "reproductive"
  match = facility_matches_need(sample_facility, user_selected_need)

  if match:
    print(f"{sample_facility['name']} matches the '{user_selected_need}' need.")
  else: 
      print(f"{sample_facility['name']} does NOT match the '{user_selcted_need}' need.")

def get_all_needs():
    return USER_HEALTH_NEEDS

