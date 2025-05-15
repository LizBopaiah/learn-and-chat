from flask import Blueprint, request, jsonify, session
from models import db, ChatHistory

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def get_history():
    history = ChatHistory.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{'id': h.id, 'question': h.question, 'answer': h.answer} for h in history])

@history_bp.route('/history', methods=['POST'])
def save_history():
    data = request.get_json()
    new_entry = ChatHistory(user_id=session['user_id'], question=data['question'], answer=data['answer'])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Chat history saved'})
