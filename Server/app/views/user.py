from flask import Blueprint, abort, request, Response
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash

from app.models.account import UserModel
from app.views import get_200_response

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


@api.resource('/signup')
class Signup(Resource):

    def post(self):

        payload = request.json
        if not payload:
            abort(406)

        id = payload['id']
        pw = payload['pw']
        name = payload['name']
        email = payload['email']

        if UserModel.objects(id=id):
            abort(409)

        UserModel(
            id=id,
            pw=generate_password_hash(pw),
            name=name,
            email=email
        ).save()

        return Response('', 201)

#
# @api.resource('/register')
# class Register(Resource):
#     def get(self):
#         return 'Hi Register', 200
#
#     def post(self):
#         body = request.json
#         if not body:
#             return {'msg': '잘못된 입력값입니다'}
#
#         if UserModel.query.filter_by(id=body['id']).first():
#             abort(409)
#
#         user = UserModel(id=body['id'], pw=body['pw'], username=body['username'])
#         current_app.config['db'].session.add(user)
#         current_app.config['db'].session.commit()
#
#         return '', 201


@api.resource('/login')
class Login(Resource):
    def get(self):
        return 'Hi Login', 200

    def post(self):
        body = request.json
        if not body:
            return {'msg': '잘못된 입력값입니다.'}

        if UserModel.query.filter_by(id=body['id'], pw=body['pw']).first() is not None:
            return get_200_response({
                'access_token': create_access_token(identity=body['id']),
                'refresh_token': create_refresh_token(identity=body['pw'])
            })
        else:
            return {
                'msg': '아이디 또는 비밀번호가 틀렸습니다.'
            },
