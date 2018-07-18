from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect

from app import route


def create_app(*config_obj):
    app_ = Flask(__name__)

    for obj in config_obj:
        app_.config.from_object(obj)

    connect(**app_.config['MONGODB_SETTINGS'])
    # db.init_app(app_)
    # app_.config['db'] = db

    route(app_)

    JWTManager().init_app(app_)


    # with app_.app_context():
    #     db.create_all()

    return app_


