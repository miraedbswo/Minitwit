from mongoengine import *

from datetime import datetime


class UserModel(Document):
    id = StringField(
        primary_key=True
    )

    pw = StringField(
        min_length=8,
        required=True
    )

    name = StringField(
        required=True
    )

    email = StringField(
        required=True
    )

    profile_img_url = StringField(
        null=True
    )

    background_img_url = StringField(
        null=True
    )

    signup_time = DateTimeField(
        default=datetime.now
    )

    meta = {'allow_inheritance': True}


class FollowModel(Document):
    follower = ReferenceField(UserModel)
    followee = ReferenceField(UserModel)

    follow_time = DateTimeField(
        default=datetime.now
    )

