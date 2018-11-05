from .. import make_parameter, SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN


REGISTER_POST = {
    'tags': ['[User] 계정'],
    'description': '회원가입',
    'parameters': [
        make_parameter('id', 'ID'),
        make_parameter('password', '비밀번호'),
        make_parameter('name', '사용자 이름'),
        make_parameter('nickname', '사용자 닉네임'),
        make_parameter('email', '사용자 이메일')
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공',
        },
        '409': {
            'description': '회원가입 불가능(중복된 ID)'
        }
    }
}


LOGIN_POST = {
    'tags': ['[User] 계정'],
    'description': '로그인',
    'parameters': [
        make_parameter('id', 'ID'),
        make_parameter('password', '비밀번호')
    ],
    'responses': {
        '201': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}