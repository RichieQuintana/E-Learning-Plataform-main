from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from repositories.user_repository import UserRepository

auth_bp = Blueprint('auth', __name__)
user_repository = UserRepository()
auth_service = AuthService(user_repository)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    try:
        token = auth_service.login(email, password)
        return jsonify({"message": "Login successful", "token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
