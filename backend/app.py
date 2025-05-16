from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.chat import chat_bp
from routes.pdf import pdf_bp
from routes.history import history_bp
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with env-based config in production

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(profile_bp, url_prefix='/api/profile')
app.register_blueprint(chat_bp, url_prefix='/api/chat')
app.register_blueprint(pdf_bp, url_prefix='/api/pdf')
app.register_blueprint(history_bp, url_prefix='/api/history')

# Serve React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    dist_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    if path != "" and os.path.exists(os.path.join(dist_dir, path)):
        return send_from_directory(dist_dir, path)
    else:
        return send_from_directory(dist_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
