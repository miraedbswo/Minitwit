from flask import g, Response
import json


def get_200_response(data):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=200,
        content_type='application/json;charset=utf-8'
    )


