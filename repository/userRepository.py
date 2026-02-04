from models.user import User
from extensions import db

class UserRepository:
    @staticmethod
    def create(username, email, password):
        user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()
        return user