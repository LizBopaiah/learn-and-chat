from flask import Blueprint, request, jsonify, session
from werkzeug.utils import secure_filename
import os
from utils.pdf_processor import save_and_extract_text

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join('uploads', filename)
    file.save(filepath)
    save_and_extract_text(filepath, session['user_id'])
    return jsonify({'message': 'PDF uploaded and processed successfully'})
