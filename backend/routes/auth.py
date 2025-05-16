from flask import Blueprint, request, jsonify
from models import create_user, get_user
import hashlib

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if get_user(email):
        return jsonify({'message': 'User already exists'}), 409

    user = create_user(name, email, password)
    return jsonify({'message': 'User created successfully', 'user': user}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    hashed_input_pw = hashlib.sha256(password.encode()).hexdigest()
    if user['password'] != hashed_input_pw:
        return jsonify({'message': 'Incorrect password'}), 401

    return jsonify({'message': 'Login successful', 'user': user}), 200
