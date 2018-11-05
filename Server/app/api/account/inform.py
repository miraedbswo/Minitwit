from flask import abort, request
from flasgger import swag_from
from werkzeug.security import check_password_hash, generate_password_hash

from app.api import BaseResource, get_user_inform, json_required
from app.docs.account.inform import CHANGE_PW_POST, CHANGE_NICKNAME_POST


class ChangePWView(BaseResource):
    @swag_from(CHANGE_PW_POST)
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


class ChangeNicknameView(BaseResource):
    @swag_from(CHANGE_NICKNAME_POST)
    @get_user_inform
    @json_required({'current_nickname': str, 'new_nickname': str})
    def post(self):
        payload = request.json

        current_nickname = payload['current_nickname']
        new_nickname = payload['new_nickname']

        if g.user.nickname is not current_nickname:
            abort(403)

        if current_nickname == new_nickname:
            abort(409)

        g.user.update(pw_hashed=generate_password_hash(new_nickname))

        return '', 200
