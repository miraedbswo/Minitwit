from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token, \
                               get_jwt_identity, jwt_refresh_token_required
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.api import json_required, BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/auth'


@api.resource('/signup')
class Signup(BaseResource):
    @json_required({'id': str, 'pw': str, 'name': str, 'email': str})
    def post(self):
        payload = request.json

        id = payload['id']
        pw = payload['pw']
        name = payload['name']
        email = payload['email']

        if UserModel.objects(id=id).first():
            abort(409)

        try:
            hashed_pw = generate_password_hash(pw)

            UserModel(
                id=id,
                pw=hashed_pw,
                name=name,
                email=email
            ).save()
        except TypeError:
            abort(400)

        return Response('', 201)


@api.resource('/login')
class Login(BaseResource):
    def post(self):
        payload = request.json

        user_id = payload['id']
        user_pw = payload['pw']

        user = UserModel.objects(id=user_id).first()
        self.check_is_exist(user)

        if check_password_hash(user.pw, user_pw):
            abort(406)

        return {
            'access_token': create_access_token(user.id),
            'refresh_token': create_refresh_token(user.id)
        }, 200


@api.resource('/refresh')
class GetRefreshToken(BaseResource):
    @jwt_refresh_token_required
    def get(self):
        user = UserModel.objects(id=get_jwt_identity()).first()
        self.check_is_exist(user)

        return {
            'access_token': create_access_token(identity=user.id),
        }
