from flask import g, Response
import json
import logging
from logging.handlers import RotatingFileHandler


def route(app):
    from api import user
    app.register_blueprint(user.api.blueprint)
    from api import post
    app.register_blueprint(post.api.blueprint)


def get_200_response(data):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=200,
        content_type='application/json;charset=utf-8'
    )


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
