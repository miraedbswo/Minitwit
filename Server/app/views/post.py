from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required

from datetime import datetime

from app.views import BaseResource
from app.models.account import UserModel
from app.models.post import CommentModel, PostModel

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/post')
class HandleRequests(BaseResource):
    @jwt_required
    def get(self):

        user = UserModel.objects(id=get_jwt_identity()).first()
        all_post = PostModel.objects(author=user.name).all()

        return self.unicode_safe_json_dumps([{
            'obj_id': str(post.id),
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': post.comments,
            'timestamp': str(post.timestamp)
        } for post in all_post], 200) if user or all_post else abort(406)

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
            timestamp=datetime.now()
        ).save()
        return Response('', 201)


@api.resource('/post/<obj_id>')
class PostObject(BaseResource):
    @jwt_required
    def get(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        comment = post.comments
        comments = []

        for data in comment:
            name = str(data['name'])
            comment = str(data['comment'])

            one_comment = {
                "name": name,
                "comment": comment
            }
            comments.append(one_comment)

        return self.unicode_safe_json_dumps({
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': comments,
            'timestamp': str(post.timestamp)
        }, 200)

    @jwt_required
    def post(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        user = UserModel.objects(id=get_jwt_identity()).first()

        comment = CommentModel(
            name=user.name,
            comment=request.json['comment'],
        )

        post.comments.append(comment)
        post.save()

        return '', 201

