from flask_restful import Resource, Api
from flask import Blueprint, Response

import json

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/post'


@api.resource('/')
class Posting(Resource):
    def get(self):
        return Response(
            json.dumps({
                'msg': '송진우 짜증나'
            }, ensure_ascii=False),
            status=200,
            content_type='application/json;charset=utf-8'
        )

    def post(self):
        pass


@api.resource('/<int:num>')
class In_post(Resource):
    def get(self, num: int):
        return {
            "data": num
        }, 200

    def post(self):
        pass
