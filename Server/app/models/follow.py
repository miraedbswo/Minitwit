from datetime import datetime

from mongoengine import *

from app.models.account import UserModel


class FollowModel(Document):
    """
    follower = 팔로우 하는 사람
    followee = 팔로우 받는 사람
    """
    follower = ReferenceField(
        UserModel
    )

    followee = ReferenceField(
        UserModel
    )

    follow_time = DateTimeField(
        default=datetime.now
    )


