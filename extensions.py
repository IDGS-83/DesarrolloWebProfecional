from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API",
        "description": "api del 83",
        "version": "1.0"
    },
    # must be lowercase `securityDefinitions` for Swagger 2.0
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "AQUI VA Bearer <token>"
        }
    },
    # apply the BearerAuth scheme globally so the lock button appears
    "security": [{
        "BearerAuth": []
    }]
}

swagger = Swagger(template=swagger_template)

# JWT extension instance (initialized later)
jwt = JWTManager()
