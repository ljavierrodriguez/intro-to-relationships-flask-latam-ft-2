from flask import Blueprint, request, jsonify

api = Blueprint("api", __name__)

@api.route('/status', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_status():
    return jsonify({ "status": "success" }), 200