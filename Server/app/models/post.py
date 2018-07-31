from mongoengine import *


class PostModel(Document):

    title = StringField(
        max_length=100,
    )
    # Post의 제목

    author = StringField()
    # 작성자

    content = StringField()
    # 작성할 글

    timestamp = StringField()
    # Post 올라온 시간

    meta = {
        'allow_inheritance': True
    }
