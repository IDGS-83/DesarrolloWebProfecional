from flask import Flask
from extensions import db, migrate, swagger, jwt
from config import Config
from controllers.AuthController import auth_bp
from controllers.UserController import user_bp
from settings.aws_secret import AwsSecretManager
import os

def create_app():
    app = Flask(__name__)

    # ===============================
    # Database configuration
    # ===============================
    try:
        aws_secret = AwsSecretManager()
        secreto = aws_secret.get_secret(os.getenv("SECRET_NAME"))

        print("Secreto cargado desde AWS:", secreto)

        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{secreto['user']}:{secreto['password']}"
            f"@{secreto['host']}:{os.getenv('AWS_PORT', 3306)}/{secreto['db']}"
        )
    except Exception as e:
        print("No se pudo cargar secreto AWS, usando .env:", e)
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.LOCAL_DB_URI

    # ===============================
    # Flask & Extensions config
    # ===============================
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # ⚠️ JWT_SECRET_KEY NO se usa para Cognito
    # Flask-JWT-Extended solo valida tokens entrantes
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]

    # ===============================
    # Init extensions
    # ===============================
    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    jwt.init_app(app)

    # ===============================
    # Blueprints
    # ===============================
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
