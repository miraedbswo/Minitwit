from flask import Blueprint, abort, request, redirect, url_for
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required

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

        user = UserModel.objects(id=get_jwt_identity()).first()
        all_post = PostModel.objects(author=user.name).all()

        if user is None or all_post is None:
            abort(406)

        return self.unicode_safe_json_dumps([{
            'obj_id': post.id.__str__(),
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': post.comments,
            'timestamp': post.timestamp.__str__()
        } for post in all_post], 200)

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
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        ).save()

        return self.unicode_safe_json_dumps({
            "msg": "게시물 작성이 완료되었습니다.",
        }, 201)


@api.resource('/<obj_id>')
class PostObject(BaseResource):
    @jwt_required
    def get(self, obj_id):

        post = PostModel.objects(id=obj_id).first()

        return self.unicode_safe_json_dumps({
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': post.comments,
            'timestamp': post.timestamp.__str__()
        }, 200)
