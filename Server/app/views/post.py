from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required

from app.views import BaseResource
from app.models.post import Comment, PostModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/post'


@api.resource('/')
class PostCombine(BaseResource):
    def get(self):
        return self.unicode_safe_json_dumps({
            'msg': '한글 유니코드 안 깨지는지 테스트'
        })

    def post(self):
        pass
        # post 한 내용 모두 다 띄워주는 기능


@api.resource('/')
class Posting(BaseResource):
    @jwt_required
    def post(self):
        payload = request.json

        if not payload:
            abort(409)

        title = payload['title']
        content = payload['content']

        new_posting = PostModel(
            title=title,
            # author= 설정 해야 함
            content=content
        ).save()

        return {
            'id': str(new_posting.id)
        }, 201
        pass


@api.resource('/<int:num>')
class In_post(BaseResource):
    def get(self, num: int):
        return {
            "data": num
        }, 200

    def post(self):
        pass
