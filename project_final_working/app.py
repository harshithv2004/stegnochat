from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from steganography import encode_image, decode_image
from PIL import Image

# MySQL
import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy

# ---------------- Flask App Initialization ----------------
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Upload settings
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:your_password(****)@localhost/stegochat"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)


# ---------------- Database Models ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.String(120), nullable=False)
    user2 = db.Column(db.String(120), nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))
    sender = db.Column(db.String(120))
    message = db.Column(db.Text)
    image = db.Column(db.String(255))
    decoded_message = db.Column(db.Text)


# ---------------- Helper Functions ----------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def save_as_png(uploaded_file):
    filename = secure_filename(uploaded_file.filename)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    uploaded_file.save(temp_path)

    img = Image.open(temp_path).convert("RGB")
    png_filename = os.path.splitext(filename)[0] + ".png"
    png_path = os.path.join(app.config['UPLOAD_FOLDER'], png_filename)
    img.save(png_path, format="PNG")

    if temp_path != png_path and os.path.exists(temp_path):
        os.remove(temp_path)

    return png_filename, png_path


def get_or_create_chat(user1, user2):
    chat = Chat.query.filter(
        ((Chat.user1 == user1) & (Chat.user2 == user2)) |
        ((Chat.user1 == user2) & (Chat.user2 == user1))
    ).first()

    if not chat:
        chat = Chat(user1=user1, user2=user2)
        db.session.add(chat)
        db.session.commit()

    return chat


# ---------------- Routes ----------------
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if User.query.filter_by(username=username).first():
            return render_template('register.html', error="Username already exists")

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return render_template('register.html', success=True)

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('chat'))

        return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        receiver = request.form['receiver'].strip()
        message = request.form['message'].strip()
        hidden_message = request.form['hidden_message'].strip()
        image = request.files.get('image')

        if not receiver or not message:
            return render_template('chat.html', username=username, chats=[], error="Receiver and message are required")

        receiver_user = User.query.filter_by(username=receiver).first()
        if not receiver_user:
            return render_template('chat.html', username=username, chats=[], error="Receiver does not exist")

        chat = get_or_create_chat(username, receiver)
        image_filename = None
        decoded_message = None

        if image and allowed_file(image.filename):
            try:
                image_filename, image_path = save_as_png(image)

                encoded_image = encode_image(image_path, hidden_message)
                encoded_image.save(image_path, format="PNG")

                decoded_message = decode_image(image_path)

            except Exception as e:
                return f"Internal server error: {e}", 500

        new_msg = Message(
            chat_id=chat.id,
            sender=username,
            message=message,
            image=image_filename,
            decoded_message=decoded_message
        )

        db.session.add(new_msg)
        db.session.commit()

    # Load chats
    chats_data = []
    chats = Chat.query.filter((Chat.user1 == username) | (Chat.user2 == username)).all()

    for c in chats:
        msgs = Message.query.filter_by(chat_id=c.id).all()
        chats_data.append({
            "user1": c.user1,
            "user2": c.user2,
            "messages": msgs
        })

    return render_template('chat.html', username=username, chats=chats_data)


@app.route('/encode_message', methods=['POST'])
def encode_message_route():
    image = request.files['image']
    message = request.form['message']

    if image and allowed_file(image.filename):
        filename, image_path = save_as_png(image)
        encoded_image = encode_image(image_path, message)
        encoded_image.save(image_path, format="PNG")

        return jsonify({"message": "Image encoded successfully!", "image": filename})

    return jsonify({"error": "Invalid file"}), 400


@app.route('/decode_message', methods=['POST'])
def decode_message_api():
    image = request.files['image']

    if image and allowed_file(image.filename):
        filename, image_path = save_as_png(image)
        decoded_message = decode_image(image_path)
        return jsonify({"decoded_message": decoded_message})

    return jsonify({"error": "Invalid file"}), 400


# ---------------- Run App ----------------
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Correct way to create tables
    with app.app_context():
        db.create_all()

    app.run(debug=True)