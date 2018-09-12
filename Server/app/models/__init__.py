from mongoengine import *

from datetime import datetime


class BaseModel(Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    creation_time = DateTimeField(
        default=datetime.now()
    )
