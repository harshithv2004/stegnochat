#  StegoChat — secure Messaging App

**StegoChat** is a Flask-based web application that allows users to send messages with hidden text embedded inside images using LSB (Least Significant Bit) steganography.  
A simple, secure, and educational demonstration of covert communication.

##  Features
- User registration & login  
- Send normal + hidden messages  
- Encode/Decode hidden text inside images  
- Auto converts images to PNG  
- Built-in decoding for verification  
- Clean Bootstrap UI  

##  How Steganography Works
- Hidden text → UTF-8 → Base64 → Bitstream  
- Bits embedded in the least significant bits of pixels  
- STOP marker marks end of data  
- Receiver decodes the message using the app  

##  Tech Stack
- Python, Flask  
- HTML, CSS, Bootstrap  
- Pillow (PIL)  
- JSON storage  

##  Project Structure
/project  
│── app.py  
│── steganography.py  
│── users.json  
│── chats.json  
│── /static  
│     └── /uploads  
│     └── /css/style.css  
│── /templates  
     ├── index.html  
     ├── login.html  
     ├── register.html  
     └── chat.html  

##  Installation
### 1. Clone the repository  
git clone <your-repo-url>  
cd stegochat  

### 2. Install dependencies  
pip install -r requirements.txt  

### 3. Run the application  
python app.py  

Open http://127.0.0.1:5000/

## ▶ Usage
1. Register/login  
2. Select a user  
3. Write message  
4. Add hidden message  
5. Upload image  
6. Receiver decodes it  

## Author
Harshith Veerapur  
