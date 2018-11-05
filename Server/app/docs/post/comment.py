from .. import make_parameter, jwt_header


WRITE_COMMENT_POST = {
    'tags': ['[User] 게시글'],
    'description': '특정 게시글에 댓글 달기',
    'parameters': [
        jwt_header,
        make_parameter('comment', '댓글')
    ],
    'responses': {
        '201': {
            'description': '게시글 작성 성공'
        },
        '406': {
            'description': '요청 데이터 타입 오류'
        }
    }
}

ONE_COMMENT_DELETE = {
    'tags': ['[User] 게시글 관리'],
    'description': '특정 게시글에 댓글 삭제',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '게시글 삭제 성공'
        },
        '406': {
            'description': '요청 데이터 타입 오류'
        }
    }
}
