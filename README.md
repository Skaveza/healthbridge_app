# HealthBridge App API
#
# This project ranks health facilities based on user health needs and location.
# The API is built with Flask and uses Flasgger to provide Swagger UI documentation.
#
# ---- Features ----
# - Load health facility data from JSON
# - Accept user health need and location to rank nearby facilities
# - Outputs ranked list with match score, safety, and distance info
#
# ---- Prerequisites ----
# - Python 3.7 or higher
# - Git (optional, for cloning repo)
#
# ---- Setup & Run Instructions ----

# 1. Clone the repository
git clone https://github.com/Skaveza/healthbridge_app.git
cd healthbridge_app

# 2. Create Python virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install required Python packages
pip install -r requirements.txt

# 5. Run the Flask app
python app.py

#
# ---- How to Use the API ----
# - Access Swagger UI at: http://127.0.0.1:5000/apidocs
# - Use the /rank_facilities POST endpoint to submit your health need and location
#   JSON Example:
#   {
#     "need_value": "pediatrics",
#     "user_location": {"lat": -1.29, "lng": 36.82}
#   }
#
# The API will respond with a ranked list of facilities tailored to your needs.
#
# ---- Notes ----
# - Update the repo URL to your actual repository before cloning
# - facilities.json must be present in the project root directory
# - health_needs.py contains health needs definitions
#
# ---- Troubleshooting ----
# - Ensure Python 3 is installed and accessible as python3
# - If virtualenv commands fail, install venv: sudo apt-get install python3-venv
# - Check firewall or port conflicts if Flask server doesn't start properly
#
# Enjoy your Health Bridge Version1 API!
