from flask import abort, Response
from flask_restful import Resource

import json


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        """
        json 형식에서 utf-8 형식 한글이 깨지는 현상 방지.
        한글을 json 으로 보낼 때 unicode_safe_json_dumps를 사용한다.

        :param data: json type (dict)
        """
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def check_is_exist(cls, data):
        if data is None:
            abort(406)


class Router:
    """
    기능 별 blueprint 들을 모아서 register 해주는 class 구현.

    :param app: A flask application
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views import auth
        app.register_blueprint(auth.api.blueprint)
        from app.views import post
        app.register_blueprint(post.api.blueprint)
        from app.views import account
        app.register_blueprint(account.api.blueprint)
