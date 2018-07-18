from flask import g, Response
from flask_restful import Resource
import json


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls, data):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status=200,
            content_type='application/json; charset=utf8'
        )
