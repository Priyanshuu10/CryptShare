from flask import Flask, render_template, request, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from datetime import datetime
import os

from crypto_utils import encrypt_file, decrypt_file
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
files_col = db[config.COLLECTION]

os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    password = request.form['password']
    expiry = request.form['expiry']

    raw_data = file.read()
    encrypted_data, encrypted_key, iv = encrypt_file(raw_data)

    file_path = os.path.join(config.UPLOAD_FOLDER, file.filename)
    with open(file_path, 'wb') as f:
        f.write(iv + encrypted_data)

    files_col.insert_one({
        "filename": file.filename,
        "encrypted_key": encrypted_key,
        "password_hash": generate_password_hash(password),
        "expiry": datetime.fromisoformat(expiry),
        "uploaded_at": datetime.utcnow()
    })

    return render_template('success.html', filename=file.filename)

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    record = files_col.find_one({"filename": filename})

    if not record:
        return "File not found"

    if datetime.utcnow() > record['expiry']:
        return "Link expired"

    if request.method == 'POST':
        if not check_password_hash(record['password_hash'], request.form['password']):
            return "Incorrect password"

        file_path = os.path.join(config.UPLOAD_FOLDER, filename)
        with open(file_path, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()

        decrypted = decrypt_file(encrypted_data, record['encrypted_key'], iv)
        temp_file = f"temp_{filename}"
        with open(temp_file, 'wb') as f:
            f.write(decrypted)

        return send_file(temp_file, as_attachment=True)

    return render_template('download.html')
    
if __name__ == '__main__':
    app.run(debug=True)