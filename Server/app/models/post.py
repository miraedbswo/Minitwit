from mongoengine import *


class CommentModel(EmbeddedDocument):
    name = StringField()

    comment = StringField(
        default=[]
    )


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

    comments = ListField(
        EmbeddedDocumentField(CommentModel),
    )

    tags = ListField(
        default=None
    )

    timestamp = DateTimeField()
    # Post 올라온 시간

    meta = {
        'allow_inheritance': True
    }

