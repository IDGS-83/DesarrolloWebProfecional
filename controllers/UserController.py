from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flasgger import swag_from

user_bp = Blueprint("users", __name__)


@user_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    """
    Obtener usuario autenticado
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    responses:
      200:
        description: Información del usuario autenticado
    """
    user_id = int(get_jwt_identity())
    claims = get_jwt()

    return jsonify({
        "id": user_id,
        "username": claims.get("username")
    }), 200