import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from extensions import db, migrate, swagger, jwt
from config import Config
from controllers.AuthController import auth_bp
from controllers.UserController import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    jwt.init_app(app)

    # Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
