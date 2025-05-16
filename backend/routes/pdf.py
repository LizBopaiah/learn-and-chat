from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from models import save_pdf_text
from utils.pdf_processor import extract_text_from_pdf
import os

pdf_bp = Blueprint('pdf', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # current directory: backend/routes
UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')  # uploads at backend/uploads
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)  # resolve to absolute path
ALLOWED_EXTENSIONS = {'pdf'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@pdf_bp.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files or 'email' not in request.form:
        return jsonify({'message': 'No file or email provided'}), 400

    file = request.files['file']
    email = request.form['email']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Extract text from PDF
        text = extract_text_from_pdf(filepath)
        print("Extracted Text Preview:", text[:200])  # Log the first 200 characters for debugging

        if not text.strip():
            return jsonify({'message': 'Failed to extract text from PDF'}), 500

        # Save to database or wherever
        save_pdf_text(email, filename, text)

        return jsonify({
            'message': 'PDF uploaded and processed successfully',
            'textPreview': text[:500]  # Optional: remove in production
        }), 201
    else:
        return jsonify({'message': 'Invalid file type'}), 400
