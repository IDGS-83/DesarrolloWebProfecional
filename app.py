from flask import Flask
<<<<<<< HEAD
from controllers.homecontroller import blueprint_home
from extensions import db, migrate
from config import Config
from models.user import User
from controllers.AuthController import auth_bp
=======
from controllers.homecontroller import BlueprintHome
from extensions import db, migrate
from config import Config
from controllers.AuthController import auth_bp
from models.user import User
>>>>>>> be9b49c439a8f8a7d427627dfe323630cf1953bc

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
<<<<<<< HEAD

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(blueprint_home)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    @app.route("/")
    def home():
        return {'mensaje': 'hola mundo'}
=======
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(BlueprintHome)
    app.register_blueprint(auth_bp,url_prefix='/api/auth')
    @app.route('/')
    def home():
        return {'mensaje': 'hola mundo'}, 200
>>>>>>> be9b49c439a8f8a7d427627dfe323630cf1953bc

    return app

if __name__ == '__main__':
    app = create_app()
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0')
=======
    app.run(debug=True, host='0.0.0.0')
>>>>>>> be9b49c439a8f8a7d427627dfe323630cf1953bc
