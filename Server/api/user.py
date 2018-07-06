from flask import Blueprint, abort, current_app, request
from flask_restful import Api, Resource

from Database.Model import UserModel

blueprint = Blueprint('simple_blueprint', __name__)
api = Api(blueprint)


@api.resource('/register')
class Signup(Resource):
    def post(self):
        body = request.json

        if UserModel.query.filter_by(id=body['id']).first():
            abort(409)

        user = UserModel(id=body['id'], pw=body['pw'], username=body['username'])
        current_app.config['db'].session.add(user)
        current_app.config['db'].session.commit()

        return {
            'msg': 'success register'
        }

