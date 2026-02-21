from flask import Flask
from extensions import db, migrate, swagger
from config import Config
from controllers.AuthController import auth_bp
from controllers.UserController import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    # initialize JWT extension
    from extensions import jwt
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
