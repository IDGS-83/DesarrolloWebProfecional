from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash

class UserRepository:

    @staticmethod
    def create(username, email, password):
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)