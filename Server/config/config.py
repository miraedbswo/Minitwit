from datetime import timedelta
import socket
import os


class Config:
    SERVICE_NAME = 'Minitwit'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = True

    RUN_SETTINGS = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'uiversion': 3,
        'specs_route': '/docs',

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'test'
        },

        'host': 'localhost',
        'basePath': '/api'
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': '[User] 계정',
                'description': '계정 관련 API'
            },
            {
                'name': '[User] 계정 관리',
                'description': '계정 관리 관련 API'
            },
            {
                'name': '[User] 게시글',
                'description': '모든 권한으로 접근 가능한 게시글 관련 API'
            },
            {
                'name': '[User] 게시글 관리',
                'description': '게시글 관리 관련 API'
            }
        ]
    }

    # SQLALCHEMY_DATABASE_URI = "sqlite:///models/models.db"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'IAMASECRETKEY'

