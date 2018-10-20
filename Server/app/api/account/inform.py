from flask import abort, request
from werkzeug.security import check_password_hash, generate_password_hash

from app.api import BaseResource, get_user_inform, json_required


class ChangePWView(BaseResource):
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

