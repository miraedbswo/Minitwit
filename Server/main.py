from flask import Flask
from flask_jwt_extended import JWTManager

from api import route, log
from Models.account import db


def create_app(*config_obj):
    app_ = Flask(__name__)

    for obj in config_obj:
        app_.config.from_object(obj)

    db.init_app(app_)
    app_.config['db'] = db

    route(app_)
    log(app_)
    JWTManager(app_)

    with app_.app_context():
        db.create_all()

    return app_


