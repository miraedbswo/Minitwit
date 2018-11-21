import json

from test import BaseTC, check_status_code


class SignupTest(BaseTC):
    def signup_post(self, id_="TestID", password="TestPassWord",
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

    @check_status_code(409)
    def test_exist_id(self):
        self.signup_post()
        return self.signup_post(password="123123123", nickname="TestNickName", email="ab@abc.com")
