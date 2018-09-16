from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api import BaseResource, json_required
from app.models.account import UserModel, FollowModel

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/follower')
class Followers(BaseResource):
    @jwt_required
    def get(self):
        pass

    @jwt_required
    def post(self):
        account = UserModel.objects(id=get_jwt_identity()).first()

        pass
