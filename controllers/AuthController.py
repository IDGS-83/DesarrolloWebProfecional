import os
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from service.authService import authService
from flask_jwt_extended import jwt_required

auth_bp = Blueprint("auth", __name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "..", "docs", "auth")


@auth_bp.route("/register", methods=["POST"])
# registration should not require authentication
@swag_from(os.path.join(DOCS_DIR, "register.yml"))
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    try:
        user = authService.register(
            data["username"],
            data["email"],
            data["password"]
        )
    except ValueError as ve:
        # duplicate username/email
        return jsonify({"error": str(ve)}), 409
    except Exception as e:
        # unexpected DB error
        return jsonify({"error": "Database error"}), 500

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


@auth_bp.route("/login", methods=["POST"])
@swag_from(os.path.join(DOCS_DIR, "login.yml"))
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    result = authService.login(data.get("username"), data.get("password"))
    if not result:
        return jsonify({"message": "Invalid credentials"}), 401

    token = result["access_token"]
    user = result["user"]
    return jsonify({
        "access_token": token,
        "user": user.to_dict()
    }), 200
    data = request.get_json()
    result = authService.login(data["username"], data["password"])
    if not result:
        return jsonify({"message": "Invalid credentials"}), 401
    token = result["access_token"]
    user = result["user"]
    return jsonify({
        "access_token": token,
        "user": user.to_dict()
    }), 200

