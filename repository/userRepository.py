from models.user import User
from extensions import db

class UserRepository:
    @staticmethod
    def create(username):
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return user
