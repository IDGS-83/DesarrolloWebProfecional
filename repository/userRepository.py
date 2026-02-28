from models.user import User
from extensions import db

class UserRepository:

    @staticmethod
    def create(username, email, password):
        if User.query.filter_by(username=username).first():
            raise ValueError("Username already exists")
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists")

        user = User(username=username, email=email)
        user.set_pass(password)

        db.session.add(user)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return user

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update(id, data):
        user = User.query.get(id)
        if not user:
            return None

        if "username" in data:
            user.username = data["username"]
        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.set_pass(data["password"])

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return user

    @staticmethod
    def delete(id):
        user = User.query.get(id)
        if not user:
            return False

        db.session.delete(user)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return True