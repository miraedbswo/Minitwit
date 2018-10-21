from flask import Response, abort, request
from flask_jwt_extended import create_access_token, create_refresh_token, \
                               get_jwt_identity, jwt_refresh_token_required
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.api import json_required, BaseResource


class RegisterView(BaseResource):
    @json_required({'id': str, 'pw': str, 'name': str, 'nickname': str, 'email': str})
    def post(self):
        payload = request.json

        id = payload['id']
        pw = payload['pw']
        name = payload['name']
        nickname = payload['nickname']
        email = payload['email']

        if UserModel.objects(id=id).first():
            abort(409)

        try:
            pw_hashed = generate_password_hash(pw)

            UserModel(
                id=id,
                pw_hashed=pw_hashed,
                name=name,
                nickname=nickname,
                email=email
            ).save()
        except TypeError:
            abort(400)

        return Response('', 201)


class LoginView(BaseResource):
    @json_required({'id': str, 'pw': str})
    def post(self):
        payload = request.json

        user_id = payload['id']
        user_pw = payload['pw']

        user = UserModel.objects(id=user_id).first()
        self.check_is_exist(user)

        if not check_password_hash(user.pw_hashed, user_pw):
            abort(406)

        return {
            'access_token': create_access_token(user.id),
            'refresh_token': create_refresh_token(user.id)
        }, 200


class GetRefreshTokenView(BaseResource):
    @jwt_refresh_token_required
    def get(self):
        user = UserModel.objects(id=get_jwt_identity()).first()
        self.check_is_exist(user)

        return {
            'access_token': create_access_token(identity=user.id),
        }
