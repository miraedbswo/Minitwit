from flask import abort, request, Blueprint, g
from flask_restful import Api
from werkzeug.security import check_password_hash, generate_password_hash

from app.api import json_required, BaseResource, get_user_inform
from app.models.account import UserModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/<my_name>')
class ShowProfile(BaseResource):
    @get_user_inform
    def get(self, my_name):
        user = UserModel.objects(nickname=my_name).first()
        self.check_is_exist(user)

        return self.unicode_safe_json_dumps({
            "name": user.name
        })


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @get_user_inform
    @json_required({'current_pw': str, 'new_pw': str})
    def post(self):
        payload = request.json
        
        current_pw = payload['current_pw']
        new_pw = payload['new_pw']

        if not check_password_hash(g.user.pw_hashed, current_pw):
            abort(403)

        if current_pw == new_pw:
            abort(409)

        g.user.update(pw_hashed=generate_password_hash(new_pw))

        return '', 200
