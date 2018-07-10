from flask import Blueprint, abort, current_app, request, g, Response
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from Models.account import UserModel
import json

blueprint = Blueprint('user_blueprint', __name__, url_prefix='/user')
api = Api(blueprint)


@api.resource('/register')
class Signup(Resource):
    def get(self):
        return 'Hi Register', 200

    def post(self):
        body = request.json
        if not body:
            return {'msg': '잘못된 입력값입니다'}

        if UserModel.query.filter_by(id=body['id']).first():
            g.logger.info('Register failed')
            abort(409)

        user = UserModel(id=body['id'], pw=body['pw'], username=body['username'])
        current_app.config['db'].session.add(user)
        current_app.config['db'].session.commit()

        return '', 201


@api.resource('/login')
class Login(Resource):
    def get(self):
        return 'Hi Login', 200

    def post(self):
        body = request.json
        if not body:
            return {'msg': '잘못된 입력값입니다.'}

        if UserModel.query.filter_by(id=body['id'], pw=body['pw']).first() is not None:
            return Response(
                json.dumps({
                    'access_token': create_access_token(identity=body['id']),
                    'refresh_token': create_refresh_token(identity=body['pw'])
                }, ensure_ascii=False),
                status=200,
                content_type='application/json;charset=utf-8'
            )
        else:
            return {
                'msg': '아이디 또는 비밀번호가 틀렸습니다.'
            }
