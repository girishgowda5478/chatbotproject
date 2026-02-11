from flask import request, jsonify
from flask_jwt_extended import create_access_token

# Dummy users database
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"msg": "User already exists"}), 400

    users[username] = {
        "password": password,
        "role": "user"
    }

    return jsonify({"msg": "User registered successfully"}), 201


def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or user["password"] != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    # ✅ identity MUST be a string
    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"access_token": token})
