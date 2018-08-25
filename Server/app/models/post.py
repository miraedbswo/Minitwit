from mongoengine import *


class CommentModel(EmbeddedDocument):
    comment = StringField()


class PostModel(Document):
    title = StringField(
        max_length=100,
    )
    # Post의 제목

    author = StringField()
    # 작성자

    content = StringField(
        null=False
    )
    # 작성할 글

    comments = EmbeddedDocumentListField(
        CommentModel,
        null=True
    )

    timestamp = DateTimeField()
    # Post 올라온 시간

    meta = {
        'allow_inheritance': True
    }

