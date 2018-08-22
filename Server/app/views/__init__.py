from flask import abort, Response
from flask_restful import Resource

import json


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def check_is_exist(cls, data):
        if data is None:
            abort(406)


def router(app_):
    from app.views import auth
    app_.register_blueprint(auth.api.blueprint)
    from app.views import post
    app_.register_blueprint(post.api.blueprint)
    from app.views import account
    app_.register_blueprint(account.api.blueprint)
