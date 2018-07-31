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
    def check_user_is_exist(cls, user):
        if user is None:
            abort(406)
