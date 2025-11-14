#StegoChat 

 StegoChat is a secure chat application built with Flask that allows users to send both normal messages and hidden messages inside images using LSB (Least Significant Bit) steganography.
The project combines web development + image processing + security concepts to show how steganography can be applied in real-world communication.

# Steganography Chat Application

A web-based chat application that allows users to send hidden messages within images using steganography techniques.

## Features

- User registration and login with password hashing
- Real-time chat between users
- Image upload with hidden message encoding
- Decode hidden messages from images
- Secure session management
- Supports common image formats: PNG, JPG, JPEG, GIF

##How Steganography Works

    The hidden message is converted to binary format.
    
    Each bit of the message is embedded into the least significant bit of the image’s RGB pixel values.
    
    A special stop marker (1111111111111110) is added to indicate the end of the hidden message.
    
    During decoding, the image is read pixel by pixel, extracting the binary data until the stop marker is detected and then converted back to readable text.

  ##Project Structure

    
      ├── app.py             # Main Flask application
      ├── steganography.py   # Encoding and decoding hidden messages
      ├── templates/         # HTML templates
      │   ├── index.html
      │   ├── login.html
      │   ├── register.html
      │   └── chat.html
      ├── static/            # Static files like uploaded images
      │   └── uploads/
      ├── users.json         # User data storage
      ├── chats.json         # Chat data storage
      └── README.md          # Project documentation

##How It Works

     Users register and log in.
      
     Users can send messages to each other.
     
#  StegoChat — Image Steganography Messaging App

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
