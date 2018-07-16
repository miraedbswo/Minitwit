from mongoengine import *

from datetime import datetime


class Comment(EmbeddedDocument):
    content = StringField()

    name = ReferenceField(
        document_type='UserModel',
        primary_key=True
    )

    uptime = DateTimeField(
        default=datetime.now
    )


class Post(Document):
    title = StringField(
        max_length=100,
        primary_key=True
    )
    # Post의 제목

    author = ReferenceField(
        document_type='UserModel',
    )
    # 작성자

    comments = ListField(
        EmbeddedDocumentListField(Comment)
    )
    # 덧글

    meta = {
        'allow_inheritance': True
    }


class TextPost(Post):
    body = StringField()

