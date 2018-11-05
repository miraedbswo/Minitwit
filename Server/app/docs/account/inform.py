from .. import jwt_header, make_parameter


CHANGE_PW_POST = {
    'tags': ['[User] 계정 관리'],
    'description': 'User 비밀번호 변경',
    'parameters': [
        jwt_header,
        make_parameter('current_pw', '현재 비밀번호'),
        make_parameter('new_pw', '새로운 비밀번호')
    ],
    'responses': {
        '200': {
            'description': '비밀번호 변경 성공',
        },
        '403': {
            'description': '비밀번호 변경 실패(기존 비밀번호 틀림), 또는 권한 없음'
        },
        '409': {
            'description': '기존 비밀번호와 새로운 비밀번호가 일치'
        }
    }
}


CHANGE_NICKNAME_POST = {
    'tags': ['[User] 계정 관리'],
    'description': 'User 닉네임 변경',
    'parameters': [
        jwt_header,
        make_parameter('current_nickname', '현재 닉네임'),
        make_parameter('new_nickname', '새로운 닉네임')
    ],
    'responses': {
        '200': {
            'description': '닉네임 변경 성공',
        },
        '403': {
            'description': '닉네임 변경 실패(기존 비밀번호 틀림), 또는 권한 없음'
        },
        '409': {
            'description': '기존 닉네임와 새로운 닉네임이 일치'
        }
    }
}