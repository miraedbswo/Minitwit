from flask import g

from app.api import BaseResource, get_user_inform
from app.models.account import UserModel


class ShowMyProfileView(BaseResource):
    @get_user_inform
    def get(self):
        user = UserModel.objects(nickname=g.user.nickname).first()
        self.check_is_exist(user)

        return self.unicode_safe_json_dumps({
            "name": user.name
        })
