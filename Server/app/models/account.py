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

    signup_time = DateTimeField(
        default=datetime.now
    )

    is_admin = BooleanField(
        default=False
    )

    meta = {
        'allow_inheritance': True
    }
