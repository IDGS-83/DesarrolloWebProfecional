from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def name():
        return {'mensaje': 'hola mundo'}, 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')