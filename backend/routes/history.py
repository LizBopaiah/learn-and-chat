from flask import Blueprint, request, jsonify
from models import get_chat_history, rename_chat_folder

history_bp = Blueprint('history', __name__)

@history_bp.route('/get', methods=['GET'])
def get_history():
    email = request.args.get('email')
    if not email:
        return jsonify({'message': 'Email is required'}), 400

    history = get_chat_history(email)
    return jsonify({'history': history})

@history_bp.route('/rename-folder', methods=['POST'])
def rename_folder():
    data = request.get_json()
    email = data.get('email')
    old_name = data.get('old_folder_name')
    new_name = data.get('new_folder_name')

    if not all([email, old_name, new_name]):
        return jsonify({'message': 'Email, old folder name, and new folder name are required'}), 400

    success = rename_chat_folder(email, old_name, new_name)
    if success:
        return jsonify({'message': f'Folder renamed from {old_name} to {new_name}'})
    else:
        return jsonify({'message': 'Folder rename failed'}), 400
