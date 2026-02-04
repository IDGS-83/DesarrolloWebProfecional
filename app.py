from flask import Flask
from controllers.homecontroller import BlueprintHome
from extensions import db, migrate
from config import Config
from controllers.AuthController import auth_bp
from models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(BlueprintHome)
    app.register_blueprint(auth_bp,url_prefix='/api/auth')
    @app.route('/')
    def home():
        return {'mensaje': 'hola mundo'}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
