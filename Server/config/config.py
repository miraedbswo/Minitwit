import socket
import os


class Config:
    SERVICE_NAME = 'Minitwit'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = False

    RUN_SETTINGS = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

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

