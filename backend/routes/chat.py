from flask import Blueprint, request, jsonify
from models import save_chat_history, get_chat_history, get_pdf_text
from utils.pdf_processor import search_in_pdf_text
from utils.google_search import google_search_fallback

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    email = data.get('email')
    question = data.get('question')

    # Search in uploaded PDFs first
    pdf_texts = get_pdf_text(email)
    answer = None
    for filename, text in pdf_texts.items():
        found = search_in_pdf_text(text, question)
        if found:
            answer = found
            break

    # Fallback to Google Search API if no PDF answer found
    if not answer:
        answer = google_search_fallback(question)

    # Save chat history under default folder 'General'
    save_chat_history(email, 'General', question, answer)

    return jsonify({'answer': answer})
