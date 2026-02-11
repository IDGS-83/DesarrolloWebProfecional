from flask import Blueprint, jsonify
from service.userService import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        for user in users
    ]), 200