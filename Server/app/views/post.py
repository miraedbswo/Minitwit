from flask import Blueprint, abort, request, redirect, url_for
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine import *

from app.views import BaseResource
from app.models.account import UserModel
from app.models.post import Comment, PostModel

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

        title = payload['title']
        content = payload['content']

        user = UserModel.objects(id=get_jwt_identity()).first()

        new_posting = PostModel(
            title=title,
            author=user.name,
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
