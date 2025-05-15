from flask import Blueprint, request, jsonify, session
from utils.pdf_processor import extract_text_from_pdfs
from utils.google_search import google_search

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/question', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data['question']
    # Check PDFs for answer
    pdf_text = extract_text_from_pdfs(session['user_id'])
    if question in pdf_text:
        return jsonify({'answer': 'Answer found in uploaded PDFs.'})
    # Fallback to Google Search
    search_results = google_search(question)
    return jsonify({'answer': search_results})
