from functools import wraps
# from uuid import UUID
import json

from flask import Response, abort, g, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.account import UserModel

# from app.models.token import AccessTokenModel

# def auth_required(model):
#     def decorator(func):
#         @wraps(func)
#         @jwt_required
#         def wrapper(*args, **kwargs):
#             try:
#                 token = AccessTokenModel.objects(
#                     identity=UUID(get_jwt_identity())
#                 ).first()
#                 account = token.key.owner
#
#                 if not token:
#                     abort(401)
#                 if not isinstance(account, model):
#                     abort(403)
#
#             except ValueError:
#                 abort(422)
#
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


def get_user_inform(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        user = UserModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(422)
        g.user = user
        return fn(*args, **kwargs)
    return wrapper


def json_required(required_keys: dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for key, typ in required_keys.items():
                if key not in request.json:
                    return Response('{} key is required.'.format("'" + key + "'"), 400)

                if isinstance(typ, type):
                    if not isinstance(request.json[key], typ):
                        return Response('{} key only accepts {} values.'
                                        .format("'" + str(key) + "'", str(typ)[8:-2]), 406)
                else:
                    abort(400)

            return func(*args, **kwargs)
        return wrapper
    return decorator


class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        """
        json 형식에서 utf-8 형식 한글이 깨지는 현상 방지.
        한글을 json 으로 보낼 때 unicode_safe_json_dumps를 사용한다.

        :param data: json type (dict)
        :param status_code: http status code
        """

        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def check_is_exist(cls, *args):
        for data in args:
            if not data:
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
        from app.api import account
        app.register_blueprint(account.api.blueprint)
        from app.api import auth
        app.register_blueprint(auth.api.blueprint)
        from app.api import follow
        app.register_blueprint(follow.api.blueprint)
        from app.api import post
        app.register_blueprint(post.api.blueprint)
