from service.authService import authService
from flask import Blueprint, jsonify, request
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['POST'])
@swag_from({
    "tags": ["Auth"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"}
                },
                "required": ["username", "email", "password"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "Usuario creado"
        }
    }
})
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    required = ["username", "email", "password"]
    if not all(k in data for k in required):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    user = authService.register(data['username'], data['email'], data['password'])

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 201


def get_user_by_id(id):
    user = authService.find_by_id(id)

    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200

    return jsonify({'error': 'User not found'}), 404