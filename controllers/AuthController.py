from service.authService import authService
from flask import Blueprint, jsonify, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = authService.register(data['username'], data['email'], data['password'])
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

@auth_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = authService.get_user_by_id(id)
    
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    return jsonify({
        'id': user.id, 
        'username': user.username, 
        'email': user.email
    }), 200