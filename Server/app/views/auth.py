from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, \
                               get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.views import BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/auth'


@api.resource('/signup')
class Signup(BaseResource):
    def get(self):
        return 'hi', 200

    def post(self):
        payload = request.json

        id = payload['id']
        pw = payload['pw']
        pw_re = payload['pw_re']
        name = payload['name']
        uuid = payload['uuid']

        if UserModel.objects(id=id).first():
            return self.unicode_safe_json_dumps({
                "msg": '중복된 id 값입니다.'
            }, 409)

        if pw != pw_re:
            abort(406)

        try:
            hashed_pw = generate_password_hash(pw)

            UserModel(
                id=id,
                pw=hashed_pw,
                name=name,
                uuid=uuid
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

        self.check_is_exist(user)

        if check_password_hash(user.pw, user_pw):
            return {
                'access_token': create_access_token(identity=user_id),
                'refresh_token': create_refresh_token(identity=user_id)
            }
        else:
            abort(406)


@api.resource('/refresh')
class GetRefreshToken(BaseResource):
    @jwt_refresh_token_required
    def get(self):

        user = UserModel.objects(id=get_jwt_identity()).first()

        self.check_is_exist(user)

        return {
            'access_token': create_access_token(identity=user.id),
            'refresh_token': create_refresh_token(identity=user.id)
        }
