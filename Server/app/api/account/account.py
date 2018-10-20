from app.api import BaseResource, get_user_inform
from app.models.account import UserModel


class ShowProfileView(BaseResource):
    @get_user_inform
    def get(self, my_name):
        user = UserModel.objects(nickname=my_name).first()
        self.check_is_exist(user)

        return self.unicode_safe_json_dumps({
            "name": user.name
        })
