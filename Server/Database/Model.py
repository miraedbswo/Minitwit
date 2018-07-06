from main import db

from sqlalchemy import Column
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'UserModel'

    id = Column(db.String(10), primary_key=True, nullable=False)
    pw = Column(db.String(50), nullable=False)

    username = Column(db.String(30), nullable=False)
    signup_time = Column(db.DateTime, default=datetime.now())


db.create_all()
