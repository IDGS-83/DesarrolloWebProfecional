from repository.userRepository import UserRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta

class authService:

    @staticmethod
    def register(username, email, password):
        try:
            return UserRepository.create(username, email, password)
        except ValueError as ve:
            # bubble up for controller to handle
            raise
        except Exception:
            # other DB errors should also propagate
            raise

    @staticmethod
    def find_by_id(id):
        return UserRepository.find_by_id(id)

    @staticmethod
    def login(username, password):
        # look up user by username
        user = UserRepository.find_by_username(username)
        if not user:
            return None

        # verify password
        if not user.check_password(password):
            return None

        claims = {"username": user.username}

        token = create_access_token(
            identity=user.id,
            additional_claims=claims,
            expires_delta=timedelta(hours=8)
        )

        return {"access_token": token, "user": user}