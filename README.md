#  StegoChat — Image Steganography Messaging App

**StegoChat** is a Flask-based web application that enables users to send normal and hidden messages, where hidden text is embedded inside images using **LSB (Least Significant Bit) steganography**.  
The project uses a **SQL database** to store users and chat history, making it robust and production-ready.

---

##  Features
-  User authentication (Register/Login)  
-  Direct chat system between users  
-  Encode & decode hidden text inside images  
-  SQL database integration (SQLite/MySQL/PostgreSQL)  
-  Automatic PNG conversion for safe steganography  
-  Clean and responsive Bootstrap UI  

---

##  How Steganography Works
- Secret message → UTF-8 → Base64 → Bitstream  
- Bits embedded in the **least significant bits** of image pixels  
- A STOP marker indicates the end of hidden data  
- Users can decode the embedded message at any time  

---

## 🛠 Tech Stack

### Backend
- Python  
- Flask  
- SQLAlchemy (ORM)  
- SQLite/MySQL/PostgreSQL  

### Frontend
- HTML  
- CSS  
- Bootstrap  

### Image Processing
- Pillow (PIL)  
- NumPy  

---

##  Project Structure
```
stegochat/
│── app.py                 # Main Flask application
│── steganography.py       # LSB encode/decode logic
│── models.py              # Database models (SQLAlchemy)
│── config.py              # Database configuration (optional)
│── requirements.txt       # Dependencies
│── /migrations            # Flask-Migrate files (if enabled)
│── /static
│     ├── /uploads         # Uploaded & encoded images
│     └── /css/style.css   # Stylesheet
│── /templates
      ├── index.html
      ├── login.html
      ├── register.html
      └── chat.html
```

---

##  Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd stegochat
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize the database (SQLite example)
```bash
flask shell
from app import db
db.create_all()
```

### 4. Run the application
```bash
python app.py
```

Open in browser:  
http://127.0.0.1:5000/

---

## ▶ Usage
1. Register or log in  
2. Select a user  
3. Write your message  
4. Add hidden message if needed  
5. Upload an image  
6. Receiver decodes the hidden text  

---

##  Author
Harshith 
