import unittest
import json
import functools

from app import create_app
from config import config


class BaseTC(unittest.TestCase):
    def setUp(self):
        app = create_app(config.Config)

        app.testing = True
        self.client = app.test_client()

    def create_account(self, id_="TestID", password="TestPassWord",
                       nickname="TestNickname", email="TestEmail@gmail.com"):

        self.client.post(
            '/account/register',
            data=json.dumps(dict(
                id=id_,
                password=password,
                nickname=nickname,
                email=email
            )),
            content_type='application/json'
        )


def check_status_code(status_code: int):
    def decorator(func):
        @functools.wraps
        def wrapper(self, *args, **kwargs):
            rv = func(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)

        return wrapper
    return decorator
