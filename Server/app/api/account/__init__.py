from flask import Blueprint
from flask_restful import Api

from .account import ShowProfileView
from .auth import RegisterView, LoginView, GetRefreshTokenView
from .inform import ChangePWView

account_blueprint = Blueprint('account', __name__)
api = Api(account_blueprint)
api.prefix = '/account'

api.add_resource(ShowProfileView, '/show')

api.add_resource(RegisterView, '/register')
api.add_resource(LoginView, '/login')
api.add_resource(GetRefreshTokenView, '/refresh')

api.add_resource(ChangePWView, '/pw')
