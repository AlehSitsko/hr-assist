from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == current_app.config['ADMIN_USERNAME'] and password == current_app.config['ADMIN_PASSWORD']:
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(hours=8)
        )
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad credentials"}), 401
