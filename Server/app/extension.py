from flask_jwt_extended import JWTManager
from flasgger import Swagger
import mongoengine as db

jwt = JWTManager()
swag = Swagger()
