from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.views import BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


@api.resource('/signup')
class Signup(BaseResource):
    def get(self):
        return 'hi', 200

    def post(self):
        payload = request.json
        if not payload:
            abort(406)

        id = payload['id']
        pw = payload['pw']
        name = payload['name']
        email = payload['email']

        if UserModel.objects(id=id):
            return self.unicode_safe_json_dumps({
                "msg": '중복된 id 값입니다.'
            }, 409)

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

        return Response('회원가입 완료', 201)


@api.resource('/login')
class Login(BaseResource):
    def get(self):
        return 'hi', 200

    def post(self):
        payload = request.json

        if not payload:
            abort(406)

        user_id = payload['id']
        user_pw = payload['pw']

        user = UserModel.objects(id=user_id).first()

        if user is None:
            abort(406)

        if check_password_hash(user.pw, user_pw):
            return {
                'access_token': create_access_token(identity=user_id),
                'refresh_token': create_refresh_token(identity=user_id)
            }
        else:
            abort(406)
