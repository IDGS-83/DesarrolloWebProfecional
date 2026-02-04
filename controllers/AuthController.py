from services.AuthService import AuthService
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = AuthService.register(data['username'])
    return jsonify({
        "id": user.id,
        "username": user.username
    }), 201
