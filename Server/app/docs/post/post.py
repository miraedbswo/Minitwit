from .. import make_parameter, jwt_header


SHOW_ALL_NOTICE_GET = {
    'tags': ['[User] 게시글'],
    'description': '모든 게시물 보기',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '게시물 표시 성공',
            'examples': {
                '': [
                    {
                        "obj_id": "5ba48d5c3d86f2333026d48e",
                        "title": "오늘의 급식",
                        "author": "yoking-huamn",
                        "content": "감자",
                        "comments": [],
                        "tags": [],
                        "timestamp": "2018-09-21 15:19:08.161000"
                    },
                    {
                        "obj_id": "5bd04b7ee4df031b805f9eba",
                        "title": "제목2",
                        "author": "goming",
                        "content": "내용2",
                        "comments": [
                            {
                                "name": "김윤재",
                                "comment": "1"
                            },
                            {
                                "name": "김윤재",
                                "comment": "1"
                            },
                            {
                                "name": "김윤재",
                                "comment": "1"
                            },
                            {
                                "name": "김윤재",
                                "comment": "1"
                            },
                            {
                                "name": "김윤재",
                                "comment": "1"
                            }
                        ],
                        "tags": [],
                        "timestamp": "2018-09-21 15:19:08.161000"
                    }
                ]
            }
        },
        '204': {
            'description': '아무 게시물도 존재하지 않음'
        }
    }
}

WRITE_NOTICE_POST = {
    'tags': ['[User] 게시글'],
    'description': '게시글 작성',
    'parameters': [
        jwt_header,
        make_parameter('title', '게시글 제목'),
        make_parameter('content', '게시글 내용'),
        make_parameter('tags', '게시물 태그', param_type='list', required=False)
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

ONE_NOTICE_GET = {
    'tags': ['[User] 게시글'],
    'description': '특정 게시글 보기',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '특정 게시글 표시 성공',
            'examples': {
                '': {
                    "obj_id": "5ba48d5c3d86f2333026d48e",
                    "title": "오늘의 급식",
                    "author": "yoking-huamn",
                    "content": "감자",
                    "comments": [],
                    "tags": [],
                    "timestamp": "2018-09-21 15:19:08.161000"
                }
            }
        },
        '406': {
            'description': '요청 데이터 타입 오류'
        }
    }
}

ONE_NOTICE_DELETE = {
    'tags': ['[User] 게시글 관리'],
    'description': '특정 게시글 삭제',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '특정 게시글 삭제 성공',
        },
        '406': {
            'description': '특정 게시글이 존재하지 않음'
        }
    }
}
