from flask import Blueprint, jsonify, request
from flasgger import swag_from
from services.AuthService import authService
from flask_jwt_extended import jwt_required
import traceback

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Registro de usuario
    ---
    tags:
      - Auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      201:
        description: Usuario creado
      409:
        description: Conflicto (username o email existente)
    """
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
        return jsonify({"error": str(ve)}), 409
    except Exception as e:
        print("ERROR EN REGISTRO:")
        traceback.print_exc()
        return jsonify({"error": "Database error"}), 500

    return jsonify(user.to_dict()), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Login de usuario
    ---
    tags:
      - Auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login exitoso
      401:
        description: Credenciales inválidas
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    result = authService.login(data.get("username"), data.get("password"))
    if not result:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({
        "access_token": result["access_token"],
        "user": result["user"].to_dict()
    }), 200


@auth_bp.route("/users", methods=["GET"])
@jwt_required()
def get_all_users():
    """
    Listar usuarios
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    responses:
      200:
        description: Lista de usuarios
    """
    users = authService.get_all()
    return jsonify([u.to_dict() for u in users]), 200


@auth_bp.route("/users/<int:id>", methods=["GET"])
@jwt_required()
def get_user_by_id(id):
    """
    Obtener usuario por ID
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: Usuario encontrado
      404:
        description: Usuario no encontrado
    """
    user = authService.find_by_id(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


@auth_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    """
    Actualizar usuario
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    consumes:
      - application/json
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Usuario actualizado
      404:
        description: Usuario no encontrado
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON requerido"}), 400

    user = authService.update(id, data)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


@auth_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    """
    Eliminar usuario
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      204:
        description: Usuario eliminado
      404:
        description: Usuario no encontrado
    """
    deleted = authService.delete(id)

    if not deleted:
        return jsonify({"error": "User not found"}), 404

    return "", 204