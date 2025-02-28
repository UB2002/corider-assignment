from flask import Blueprint, request, jsonify
from app.Model.user import User
from app.Services.user_service import UserService
from app.validator import validate_object_id
from flask_pydantic import validate

user_bp = Blueprint("users", __name__)
user_service = UserService()

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users)

@user_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    error_response = validate_object_id(id)
    if error_response:
        return error_response
        
    user = user_service.get_user(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@user_bp.route('/users', methods=['POST'])
@validate()
def create_user(body: User):
    try:
        user_id = user_service.create_user(body.dict(exclude={'id'}))
        return jsonify({"id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/users/<id>', methods=['PUT'])
@validate()
def update_user(id, body: User):
    error_response = validate_object_id(id)
    if error_response:
        return error_response
        
    if user_service.update_user(id, body.dict(exclude={'id'})):
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    error_response = validate_object_id(id)
    if error_response:
        return error_response
        
    if user_service.delete_user(id):
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404