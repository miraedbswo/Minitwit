import os


class Config:
    SERVICE_NAME = 'Minitwit'

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }

    # SQLALCHEMY_DATABASE_URI = "sqlite:///models/models.db"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'IAmJWTSecretKey'

    SECRET_KEY = 'IAmSecretKey'

