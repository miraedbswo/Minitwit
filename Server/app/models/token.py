import uuid

from mongoengine import *
from flask_jwt_extended import create_access_token, create_refresh_token

from app.models.account import UserModel


class TokenModel(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    class Key(EmbeddedDocument):
        owner = ReferenceField(
            document_type=UserModel,
            required=True
        )

    key = EmbeddedDocumentField(
        document_type=Key,
        primary_key=True
    )

    identity = UUIDField(
        default=uuid.uuid4
    )

    @classmethod
    def _create_token(cls, owner):
        key = cls.Key(owner=owner)
        if cls.objects(key=key):
            cls.objects(key=key).delete()

        return cls(
            key=key
        ).save().identity

    @classmethod
    def create_access_token(cls, owner):
        return create_access_token(
            identity=str(cls._create_token(owner))
        )

    @classmethod
    def create_refresh_token(cls, owner):
        return create_refresh_token(
            identity=str(cls._create_token(owner))
        )


class AccessTokenModel(TokenModel):
    meta = {
        'collection': "AccessTokenModel"
    }


class RefreshTokenModel(TokenModel):
    meta = {
        'collection': "RefreshTokenModel"
    }
