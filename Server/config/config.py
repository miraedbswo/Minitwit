import socket
import os


class Config:
    SERVICE_NAME = 'Minitwit'

    host = socket.gethostbyname(socket.gethostname())
    port = 80

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }

    # SQLALCHEMY_DATABASE_URI = "sqlite:///models/models.db"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'IAMASECRETKEY'

