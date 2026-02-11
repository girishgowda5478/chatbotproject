import os
from memory import save_message, get_history
from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from chatbot import get_response
from auth import login, register

app = Flask(__name__)

# ---------------- JWT CONFIG ----------------
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key")



# ---------------- TEST ROUTE ----------------
@app.route("/", methods=["GET"])
def home():
    return "Secure Chatbot API running!"


# ---------------- REGISTER ----------------
@app.route("/register", methods=["POST"])
def register_user():
    return register()


# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login_user():
    return login()


# ---------------- PROTECTED CHAT ----------------
@app.route("/chat", methods=["POST"])
@jwt_required()
def chat():
    username = get_jwt_identity()
    claims = get_jwt()
    role = claims.get("role")

    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"msg": "Message is required"}), 400

    # 🔹 Get conversation history
    history = get_history(username)

    # 🔹 Generate reply USING context
    reply = get_response(user_message, history)

    # 🔹 Save conversation
    save_message(username, user_message, reply)

    return jsonify({
        "user": username,
        "role": role,
        "reply": reply,
        "context": history
    })


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
