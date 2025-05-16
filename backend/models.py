import hashlib

# In-memory mock database (replace with SQLite or other DB in production)
users = {}
chat_histories = {}
pdf_contents = {}

# User model functions
def create_user(name, email, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    users[email] = {
        'name': name,
        'email': email,
        'password': hashed_pw
    }
    return users[email]

def get_user(email):
    return users.get(email)

def update_user(email, name=None, password=None):
    if email in users:
        if name:
            users[email]['name'] = name
        if password:
            users[email]['password'] = hashlib.sha256(password.encode()).hexdigest()
        return users[email]
    return None

# Chat model functions
def save_chat_history(email, folder, question, answer):
    chat_histories.setdefault(email, {}).setdefault(folder, []).append({
        'question': question,
        'answer': answer
    })

def get_chat_history(email):
    return chat_histories.get(email, {})

def rename_chat_folder(email, old_name, new_name):
    if email in chat_histories and old_name in chat_histories[email]:
        chat_histories[email][new_name] = chat_histories[email].pop(old_name)
        return True
    return False

# PDF model functions
def save_pdf_text(email, filename, text):
    pdf_contents.setdefault(email, {})[filename] = text

def get_pdf_text(email):
    return pdf_contents.get(email, {})
