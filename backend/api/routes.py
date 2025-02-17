from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    try:
        data = [
            {"id": 1, "name": "Item A"},
            {"id": 2, "name": "Item B"},
            {"id": 3, "name": "Item C"}
        ]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "無法獲取資料", "details": str(e)}), 500
