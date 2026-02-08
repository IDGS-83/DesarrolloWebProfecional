from extensions import db
from passlib.hash import bcrypt

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

    def set_pass(self, password: str):
        self.password = bcrypt.hash(password)

