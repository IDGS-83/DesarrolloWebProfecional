from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from service.authService import authService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    claims = get_jwt()

    user = authService.sync_user(
        cognito_sub=claims["sub"],
        email=claims.get("email")
    )

    return jsonify(user.to_dict()), 200
