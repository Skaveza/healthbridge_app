from flask import Flask, request, jsonify
from flasgger import Swagger
import json
from facility_ranker import rank_facilities
from health_needs import get_all_needs

app = Flask(__name__)
swagger = Swagger(app)

# Load facilities data once
with open("facilities.json") as f:
    FACILITIES = json.load(f)

@app.route('/rank_facilities', methods=['POST'])
def rank_facilities_api():
    """
    Rank health facilities based on user need and location
    ---
    tags:
      - Facility Recommendation
    parameters:
      - name: need_value
        in: body
        required: true
        schema:
          type: object
          required:
            - need_value
            - user_location
          properties:
            need_value:
              type: string
              example: reproductive
            user_location:
              type: object
              properties:
                lat:
                  type: number
                  example: -1.29
                lng:
                  type: number
                  example: 36.82
    responses:
      200:
        description: A list of ranked facilities
    """
    data = request.get_json()
    need_value = data.get("need_value")
    user_location = data.get("user_location")

    if not need_value or not user_location:
        return jsonify({"error": "Missing 'need_value' or 'user_location'"}), 400

    ranked = rank_facilities(FACILITIES, need_value, user_location)
    return jsonify(ranked)

@app.route('/health_needs', methods=['GET'])
def list_health_needs():
    """
    Get available health needs
    ---
    tags:
      - Health Needs
    responses:
      200:
        description: A list of available health needs
        schema:
          type: array
          items:
            type: object
            properties:
              label:
                type: string
                example: Maternity and Delivery
              value:
                type: string
                example: maternity
    """
    return jsonify(get_all_needs())

if __name__ == '__main__':
    app.run(debug=True)
