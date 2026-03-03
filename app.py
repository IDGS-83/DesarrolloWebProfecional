from flask import Flask
from extensions import db, migrate, swagger
from config import Config
from controllers.AuthController import auth_bp
from controllers.UserController import user_bp
from settings.aws_secret import AwsSecretManager
import os

def create_app():
    app = Flask(__name__)

    try:
        aws_secret = AwsSecretManager()
        secreto = aws_secret.get_secret(os.getenv("SECRET_NAME"))

        print("Secreto cargado desde AWS:", secreto)

        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{secreto['user']}:{secreto['password']}"
            f"@{secreto['host']}:3306/{secreto['db']}"
        )

    except Exception as e:
        print("No se pudo cargar secreto AWS, usando .env:", e)
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.LOCAL_DB_URI

    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)

    from extensions import jwt
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)