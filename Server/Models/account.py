from mongoengine import *
from datetime import datetime


class UserModel(Document):

    id = StringField(
        primary_key=True
    )
    # 유저 id
    
    pw = StringField(
        min_length=8,
        max_length=20
    )
    # 유저 pw

    name = StringField(
        required=True
    )
    # 유저 이름

    email = StringField(
        required=True
    )
    # 유저 email

    signup_time = DateTimeField(
        default=datetime.now()
    )
    # 회원 가입 시간

    meta = {
        'allow_inheritance': True
    }
