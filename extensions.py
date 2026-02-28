from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API 83",
        "description": "Documentación de la API del grupo 83",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Token JWT. Formato: Bearer <token>"
        }
    },
    "security": [{"BearerAuth": []}],
    "basePath": "/",
    "schemes": ["http"]
}

swagger = Swagger(template=swagger_template)
jwt = JWTManager()