from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import route
import config

db = SQLAlchemy()


def create_app(*config_obj):
    app_ = Flask(__name__)

    for obj in config_obj:
        app_.config.from_object(obj)

    db.init_app(app_)
    app_.config['db'] = db

    route(app_)

    return app_


app = create_app(config.Config())
