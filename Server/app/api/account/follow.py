from flask import Response, g
from mongoengine.queryset.visitor import Q

from app.api import BaseResource, get_user_inform
from app.models.account import UserModel
from app.models.follow import FollowModel


class FollowView(BaseResource):
    def get(self, nickname):
        owner = UserModel.objects(nickname=nickname).first()
        self.check_is_exist(owner)

        followers = FollowModel.objects(followee=owner).all()
        following = FollowModel.objects(follower=owner).all()

        if not followers or following:
            return Response('', 204)

        followers_list = [follow_model.follower.nickname for follow_model in followers]
        following_list = [follow_model.followee.nickname for follow_model in following]

        return self.unicode_safe_json_dumps({
            "followers": followers_list,
            "following": following_list
        })

    @get_user_inform
    def post(self, nickname):
        owner = UserModel.objects(nickname=nickname).first()
        self.check_is_exist(owner)

        if FollowModel.objects(Q(follower=g.user) & Q(followee=owner)).first():
            return Response('', 208)

        FollowModel(
            follower=g.user,
            followee=owner
        ).save()

        return Response('', 201)

    @get_user_inform
    def delete(self, nickname):
        owner = UserModel.objects(nickname=nickname).first()
        self.check_is_exist(owner)

        follow = FollowModel.objects(Q(follower=g.user) & Q(followee=owner)).first()
        self.check_is_exist(follow)

        follow.delete()

        return Response('', 200)

