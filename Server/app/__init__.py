from flask import Flask

from app.api import Router
from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.jwt.init_app(flask_app)
    extension.swag.init_app(flask_app)
    extension.swag.template = flask_app.config['SWAGGER_TEMPLATE']

    extension.db.connect(**flask_app.config['MONGODB_SETTINGS'])


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)

    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    Router(flask_app)

    return flask_app


