from flask import Blueprint, Response, abort, request
from flask_restful import Api

from app.api import BaseResource, get_user_inform
from app.models.post import CommentModel, PostModel

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/post')
class HandleRequests(BaseResource):
    @get_user_inform
    def get(self):
        all_post = PostModel.objects().all()
        self.check_is_exist(all_post)

        return self.unicode_safe_json_dumps([{
            'obj_id': str(post.id),
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': [{
                "name": data.name,
                "comment": data.comment
            } for data in post.comments],
            'tags': post.tags,
            'timestamp': str(post.timestamp)
        } for post in all_post], 200)

    @get_user_inform
    def post(self):
        payload = request.json

        if not payload:
            abort(409)

        title = payload["title"]
        content = payload["content"]

        try:
            tags = payload['tags']
        except KeyError:
            tags = []

        PostModel(
            title=title,
            author=g.user,
            content=content,
            tags=tags
        ).save()

        return Response('', 201)


@api.resource('/post/<obj_id>')
class PostObject(BaseResource):
    @get_user_inform
    def get(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        return self.unicode_safe_json_dumps({
            'obj_id': str(post.id),
            'title': post.title,
            'author': post.author,
            'content': post.content,
            'comments': [{
                "name": data.name,
                "comment": data.comment
            } for data in post.comments],
            'tags': post.tags,
            'timestamp': str(post.timestamp)
        }, 200)

    @get_user_inform
    def post(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        comment = CommentModel(
            name=g.user.name,
            comment=request.json['comment'],
        )

        post.comments.append(comment)
        post.save()

        return '', 201

    @get_user_inform
    def delete(self, obj_id):
        post = PostModel.objects(id=obj_id).first()

        self.check_is_exist(post)
        post.delete()

        return '', 200
