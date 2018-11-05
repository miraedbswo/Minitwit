from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account', __name__)
api = Api(account_blueprint)
api.prefix = '/account'

from .account import ShowMyProfileView
api.add_resource(ShowMyProfileView, '/profile')

from .auth import RegisterView, LoginView, GetRefreshTokenView
api.add_resource(RegisterView, '/register')
api.add_resource(LoginView, '/login')
api.add_resource(GetRefreshTokenView, '/refresh')

from .inform import ChangePWView, ChangeNicknameView
api.add_resource(ChangePWView, '/pw')
api.add_resource(ChangeNicknameView)

from .follow import FollowView
api.add_resource(FollowView, '/follow/<nickname>')
