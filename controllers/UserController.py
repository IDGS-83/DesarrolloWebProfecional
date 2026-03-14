from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

user_bp = Blueprint('users', __name__)

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    claims = get_jwt()

    return jsonify({
        "cognito_sub": claims["sub"],
        "email": claims.get("email"),
        "role": claims.get("role", "user")
    }), 200
