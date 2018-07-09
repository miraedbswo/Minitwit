from flask import Flask, g
import logging
from logging.handlers import RotatingFileHandler

from api import user


def route(app):
    app.register_blueprint(user.api.blueprint)


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

        g.logger.info('<===server logging===>')
