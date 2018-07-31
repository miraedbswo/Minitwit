from flask import abort, request, Blueprint
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @jwt_required
    def post(self):

        payload = request.json

        current_pw = payload['current_pw']
        new_pw = payload['new_pw']

        user = UserModel.objects(id=get_jwt_identity()).first()

        self.check_is_exist(user)

        if not check_password_hash(user.pw, current_pw):
            abort(403)

        if current_pw == new_pw:
            abort(409)

        user.update(pw=generate_password_hash(new_pw))

        return self.unicode_safe_json_dumps({
            "msg": f"비밀번호가 {new_pw}로 변경되었습니다.",
        }, 200)
