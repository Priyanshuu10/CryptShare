# 🔐 KeyLock – Secure Encrypted File Sharing System

KeyLock is a cyber‑security focused web application that enables **secure, encrypted file sharing** with **password protection** and **time‑bound access control**. The system ensures confidentiality and controlled access to sensitive files using cryptographic principles.


## 📌 Features

* 🔒 **Encrypted File Uploads** – Files are encrypted before being stored on the server
* 🔑 **Password‑Protected Downloads** – Only users with the correct password can access files
* ⏳ **Expiry‑Based Access** – Download links automatically expire after a set time
* 🧾 **Secure Metadata Storage** – File details stored securely in MongoDB
* 🌐 **Web‑Based Interface** – Clean, responsive UI for easy interaction

---

## 🛠 Tech Stack

| Layer        | Technology                                     |
| ------------ | ---------------------------------------------- |
| Backend      | Python, Flask                                  |
| Database     | MongoDB                                        |
| Cryptography | AES (symmetric encryption), RSA (key exchange) |
| Frontend     | HTML5, CSS3                                    |
| Tools        | Git, VS Code                                   |

---

## 🧠 System Architecture

1. User uploads a file via the web interface
2. File is encrypted using AES encryption
3. Encryption key is protected using RSA
4. Encrypted file is stored on the server
5. File metadata (filename, expiry, password hash) is stored in MongoDB
6. Download access is validated using password + expiry time


## 🔐 Security Highlights

* AES encryption ensures fast and secure file encryption
* RSA secures encryption keys
* Passwords are never stored in plain text
* Time‑based expiry prevents unauthorized long‑term access


## 🚀 Future Enhancements

* User authentication
* File size validation
* Email‑based secure download links
* Audit logs for file access


## 👨‍💻 Author

**Priyanshu Pati**
B.Tech CSE | XIM University
