from flask import Flask
from controllers.HomeController import blueprint_home

def create_app():
    app = Flask(__name__)
    app.registrer_blueprint(blueprint_home)
    @app.route("/")
    def home():
        return {'mensaje': 'hola mundo'}
    
    return app

if__name__="__main__":
app = create_app()
app.run(debug=True, host='0.0.0.0')