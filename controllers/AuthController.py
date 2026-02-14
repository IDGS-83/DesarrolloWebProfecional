import os
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from service.authService import authService

auth_bp = Blueprint("auth", __name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "..", "docs", "auth")


@auth_bp.route("/register", methods=["POST"])
@swag_from(os.path.join(DOCS_DIR, "register.yml"))
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    user = authService.register(
        data["username"],
        data["email"],
        data["password"]
    )

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    }), 201


@auth_bp.route("/users", methods=["GET"])
@swag_from(os.path.join(DOCS_DIR, "get_all.yml"))
def get_all_users():
    users = authService.get_all()

    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "email": u.email
        }
        for u in users
    ]), 200


@auth_bp.route("/users/<int:id>", methods=["GET"])
@swag_from(os.path.join(DOCS_DIR, "get_user_by_id.yml"))
def get_user_by_id(id):
    user = authService.find_by_id(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    }), 200


@auth_bp.route("/users/<int:id>", methods=["PUT"])
@swag_from(os.path.join(DOCS_DIR, "update.yml"))
def update_user(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    user = authService.update(id, data)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    }), 200
