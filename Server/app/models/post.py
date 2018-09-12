from mongoengine import *

from datetime import datetime

from app.models import BaseModel
from app.models.account import UserModel


class CommentModel(EmbeddedDocument):
    user = ReferenceField(
        document_type=UserModel
    )

    comment = ListField(
        default=[]
    )


class PostModel(BaseModel):
    title = StringField(
        max_length=100,
    )
    # Post의 제목

    user = ReferenceField(
        document_type=UserModel
    )

    content = StringField(
        null=False
    )

    comments = EmbeddedDocumentListField(
        document_type=CommentModel
    )

    tags = ListField(
        default=None
    )

    timestamp = DateTimeField(
        default=datetime.now()
    )

