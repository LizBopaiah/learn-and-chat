from flask import Blueprint, request, jsonify
from models import get_user, update_user

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/<email>', methods=['GET'])
def get_profile(email):
    user = get_user(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user}), 200

@profile_bp.route('/<email>', methods=['PUT'])
def update_profile(email):
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    updated_user = update_user(email, name, password)
    if not updated_user:
        return jsonify({'message': 'Update failed'}), 400

    return jsonify({'message': 'Profile updated successfully', 'user': updated_user}), 200
