from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect
import logging
from logging.handlers import RotatingFileHandler


def route(app_):
    from app.views import user
    app_.register_blueprint(user.api.blueprint)
    from app.views import post
    app_.register_blueprint(post.api.blueprint)


def log(app):
    @app.before_request
    def before_first_request():
        def make_logger():
            handler = RotatingFileHandler('server_log.log', maxBytes=10000, backupCount=2)
            formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            app.logger.addHandler(handler)

        make_logger()
        g.logger = app.logger
        print(g.logger)

        g.logger.info('server logging')


def create_app(*config_obj):
    app_ = Flask(__name__)

    for obj in config_obj:
        app_.config.from_object(obj)

    connect(**app_.config['MONGODB_SETTINGS'])
    # db.init_app(app_)
    # app_.config['db'] = db

    route(app_)
    log(app_)

    JWTManager().init_app(app_)

    return app_


