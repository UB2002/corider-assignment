from bson import ObjectId
from flask import jsonify

def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "Invalid user ID"}), 400
    return None