import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.getenv("FLASK_ENV")
    LOCAL_DB_URI = (
        f"mysql+pymysql://{os.getenv('AWS_USER')}:{os.getenv('AWS_PASSWORD')}"
        f"@{os.getenv('AWS_HOST')}:{os.getenv('AWS_PORT')}/{os.getenv('AWS_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_ACCESS_TOKEN_EXPIRES = False