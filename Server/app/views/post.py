from flask_restful import Resource, Api
from flask import Blueprint, Response

import json

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/post'


@api.resource('/')
class Posting(Resource):
    def get(self):
        return

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
