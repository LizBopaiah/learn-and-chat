from flask import Blueprint, request, jsonify, session
from models import db, User
from werkzeug.security import generate_password_hash

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user = User.query.get(session['user_id'])
    return jsonify({'name': user.name, 'email': user.email})

@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user = User.query.get(session['user_id'])
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    if data.get('password'):
        user.password = generate_password_hash(data['password'], method='sha256')
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'})
