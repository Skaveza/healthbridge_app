# HealthBridge App API

**HealthBridge** ranks nearby health facilities based on a user's health needs and location.  
The API is built using **Flask** and documented with **Flasgger** (Swagger UI).

---

## Features

- Loads health facility data from a JSON file  
- Accepts user's health need and location as input  
- Returns a ranked list of facilities based on:
  - Match score
  - Safety rating
  - Distance from the user

---

## Quick Start

```bash
git clone https://github.com/Skaveza/healthbridge_app.git
cd healthbridge_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Access the API at: http://127.0.0.1:5000/apidocs

---

## Prerequisites

- Python 3.7 or higher  
- Git (for cloning the repository)

---

## ⚙️ Setup & Run Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Skaveza/healthbridge_app.git
cd healthbridge_app
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Flask App
```bash
python app.py
```

The app will start at: http://127.0.0.1:5000

---

## 📡 How to Use the API

### 🔗 Swagger UI
Navigate to:
```
http://127.0.0.1:5000/apidocs
```

### 📍 Endpoint: `/rank_facilities` (POST)
Use this endpoint to rank nearby health facilities based on your health need and location.

### 📥 Example JSON Request
```json
{
  "need_value": "pediatrics",
  "user_location": {
    "lat": -1.29,
    "lng": 36.82
  }
}
```

### 📤 Example JSON Response
```json
[
  {
    "facility_name": "Hope Medical Center",
    "match_score": 0.93,
    "distance_km": 2.5,
    "safety_rating": "High",
    "location": {
      "lat": -1.288,
      "lng": 36.821
    }
  }
]
```

---

## 🏥 Supported Health Needs

Available values for `need_value` include:
- `pediatrics`
- `cardiology`
- `emergency`
- `general`

*(See `health_needs.py` for the full list of supported categories.)*

---

## 📊 Ranking Criteria

Facilities are ranked using a combination of:
- **Match score** (how well the facility meets the health need)
- **Distance** (from user location)
- **Safety rating** (predefined or scored from data)

**Note:** The algorithm currently gives equal weight to each of these factors. This can be customized in future versions.

---

## 📋 API Response Codes

- **200**: Success — returns a ranked list of facilities
- **400**: Bad Request — missing or invalid input fields
- **404**: No matching facilities found for the given criteria

---

## ✅ Validation Rules

- `lat` and `lng` must be valid geographic coordinates
- `need_value` must match one of the supported health need categories
- Both fields are required in the request

---

## 📁 Data Requirements

The file `facilities.json` must be placed in the project root directory.

### Sample `facilities.json` Structure
```json
[
  {
    "facility_name": "Hope Medical Center",
    "location": {
      "lat": -1.288,
      "lng": 36.821
    },
    "services": ["pediatrics", "general", "emergency"],
    "safety_rating": "High"
  }
]
```

---

## 🛠 Troubleshooting

- Ensure Python 3 is installed and accessible via `python3`
- If `venv` creation fails, install it using:
  ```bash
  sudo apt-get install python3-venv
  ```
- If Flask doesn't start, check for firewall or port conflicts

---

## 📝 Notes

- Update the repository URL in this README if you move or fork the project
- Make sure `health_needs.py` and `facilities.json` are correctly configured

---

**🎉 Enjoy using HealthBridge API v1!**
