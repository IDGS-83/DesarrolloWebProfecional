from extensions import db
from passlib.hash import bcrypt_sha256

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

    def set_pass(self, password: str):
        self.password = bcrypt_sha256.hash(password)

    def verify_pass(self, password: str):
        return bcrypt_sha256.verify(password, self.password)