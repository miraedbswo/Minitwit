from mongoengine import *
from datetime import datetime
from uuid import uuid4


class UserModel(Document):

    id = StringField(
        primary_key=True
    )
    # 유저 id

    pw = StringField(
        min_length=8,
        required=True
    )
    # 유저 pw

    name = StringField(
        required=True
    )
    # 유저 이름

    email = StringField(
    )
    # 유저 email

    uuid = StringField()

    signup_time = DateTimeField(
        default=datetime.now
    )
    # 회원 가입 시간

    is_admin = BooleanField(
        default=False
    )

    meta = {
        'allow_inheritance': True
    }
