from flask import Flask
from controllers.homecontroller import BlueprintHome

def create_app():
    app = Flask(__name__)

    app.register_blueprint(BlueprintHome)
    @app.route('/')
    def name():
        return {'mensaje': 'hola mundo'}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')