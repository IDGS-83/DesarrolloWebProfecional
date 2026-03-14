from models.user import User
from extensions import db

class UserRepository:

    @staticmethod
    def create(cognito_sub, email, role="user"):
        user = User(
            cognito_sub=cognito_sub,
            email=email,
            role=role
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)

    @staticmethod
    def find_by_cognito_sub(sub):
        return User.query.filter_by(cognito_sub=sub).first()

    @staticmethod
    def get_all():
        return User.query.all()
