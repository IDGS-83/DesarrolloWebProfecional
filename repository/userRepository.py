from models.user import User
from extensions import db

class UserRepository:

    @staticmethod
    def create(username, email, password):
        user = User(username=username, email=email)
        user.set_pass(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)
