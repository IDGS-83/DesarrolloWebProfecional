from service.authService import authService
from flask import Blueprint, jsonify, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = authService.register(data['username'])

    return jsonify({'id': user.id, 'username': user.username}), 201
