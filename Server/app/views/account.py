from flask import abort, request, Blueprint
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.account import UserModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


# @api.resource('/<str: my_name>')
# class Mypage(BaseResource):
#     @jwt_required
#     def get(self, my_name):
#         user = UserModel.objects(name=my_name).first()
#         self.check_is_exist(user)
#
#         return self.unicode_safe_json_dumps({
#             "name": user.name,
#         })


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

        return '', 200
