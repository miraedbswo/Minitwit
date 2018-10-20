from mongoengine import *

from datetime import datetime

from app.models import BaseModel
from app.models.account import UserModel


class CommentModel(EmbeddedDocument):
    user = ReferenceField(
        document_type=UserModel
    )

    comment = StringField(
        required=True
    )

    comment_num = IntField(
        required=True,
        unique=True
    )


class PostModel(BaseModel):
    title = StringField(
        max_length=100,
    )
    # Post의 제목

    author = ReferenceField(
        document_type=UserModel
    )

    content = StringField(
        required=True
    )

    comments = EmbeddedDocumentListField(
        CommentModel
    )

    tags = ListField(
        StringField()
    )

    timestamp = DateTimeField(
        default=datetime.now
    )

