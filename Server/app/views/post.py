from flask import Blueprint, abort, request, redirect, url_for
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine import *

from datetime import datetime

from app.views import BaseResource
from app.models.account import UserModel
from app.models.post import PostModel

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/post'


@api.resource('')
class HandleRequests(BaseResource):
    @jwt_required
    def get(self):
        for post in PostModel.objects().all():
            return self.unicode_safe_json_dumps({
                'title': post.title,
                'author': post.author,
                'content': post.content,
                'comments': post.comments,
                'uptime': post.uptime
            })

    def post(self):
        return redirect(url_for(Posting))


@api.resource('/submit')
class Posting(BaseResource):
    @jwt_required
    def post(self):
        payload = request.json

        if not payload:
            abort(409)

        title = payload["title"]
        content = payload["content"]

        user = UserModel.objects(id=get_jwt_identity()).first()
        if user is None:
            abort(406)

        PostModel(
            title=title,
            author=user.name,
            content=content,
            timestamp=datetime.now().__str__()
        ).save()

        return self.unicode_safe_json_dumps({
            "msg": "게시물 작성이 완료되었습니다.",
            "nickname": user.name,
            "datetime": datetime.now().__str__()
        }, 201)


@api.resource('/<int:num>')
class Inpost(BaseResource):
    def get(self, num: int):
        return {
            "data": num
        }, 200

    def post(self):
        pass
