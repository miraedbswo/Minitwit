from mongoengine import *

from datetime import datetime


class Comment(EmbeddedDocument):
    content = StringField()
    # comment의 content

    name = ReferenceField(
        document_type='UserModel',
        primary_key=True
    )
    # 작성자

    uptime = DateTimeField(
        default=datetime.now
    )
    # 덧글 단 시간


class PostModel(Document):
    title = StringField(
        max_length=100,
    )
    # Post의 제목

    author = ReferenceField(
        document_type='UserModel',
    )
    # 작성자

    content = StringField()
    # 작성할 글

    comments = ListField(
        EmbeddedDocumentListField(Comment)
    )
    # 덧글

    uptime = DateTimeField(
        default=datetime.now
    )
    # Post 올라온 시간

    meta = {
        'allow_inheritance': True
    }
