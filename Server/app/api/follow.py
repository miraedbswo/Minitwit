from flask import Blueprint, Response
from flask_restful import Api
from mongoengine.queryset.visitor import Q

from app.api import BaseResource, get_user_inform
from app.models.account import UserModel
from app.models.follow import FollowModel

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = 'follow'


@api.resource('/<username>')
class Follow(BaseResource):
    @get_user_inform
    def get(self, username):
        owner = UserModel.objects(name=username).first()
        followers = FollowModel.objects(followee=owner).all()
        following = FollowModel.objects(follower=owner).all()

        return self.unicode_safe_json_dumps({
            "followers": [follower.name for follower in followers.follower],
            "following": [following.name for following in following.followee]
        })

    @get_user_inform
    def post(self, username):
        owner = UserModel.objects(name=username).first()
        self.check_is_exist(owner)

        if not FollowModel.objects(Q(follower=g.user) & Q(followee=owner)).first():
            return Response('', 208)

        FollowModel(
            follower=g.user,
            followee=owner
        ).save()

        return Response('', 201)

    @get_user_inform
    def delete(self, username):
        owner = UserModel.objects(name=username).first()
        self.check_is_exist(owner)

        follow = FollowModel.objects(Q(follower=g.user) & Q(followee=owner)).first()
        self.check_is_exist(follow)

        follow.delete()

        return Response('', 200)

