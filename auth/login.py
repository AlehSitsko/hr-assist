from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import os
from datetime import timedelta

auth_bp = Blueprint("auth", __name__)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1234")

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    if data.get("username") == ADMIN_USERNAME and data.get("password") == ADMIN_PASSWORD:
        tok = create_access_token(identity=data["username"], expires_delta=timedelta(hours=8))
        return jsonify({"access_token": tok}), 200
    return jsonify({"error": "Invalid credentials"}), 401
