from flask import Response, abort, request, g
from flasgger import swag_from

from app.api import BaseResource, get_user_inform, json_required
from app.models.post import PostModel
from app.docs.post.post import SHOW_ALL_NOTICE_GET, WRITE_NOTICE_POST, ONE_NOTICE_GET, ONE_NOTICE_DELETE


class ShowAllPostView(BaseResource):
    @swag_from(SHOW_ALL_NOTICE_GET)
    @get_user_inform
    def get(self):
        all_post = PostModel.objects().all()
        if not all_post:
            return Response('', 204)

        return self.unicode_safe_json_dumps([{
            'obj_id': str(post.id),
            'title': post.title,
            'author': post.author.nickname,
            'content': post.content,
            'comments': [{
                "name": data.user.name,
                "comment": data.comment
            } for data in post.comments if data],
            'tags': post.tags,
            'timestamp': str(post.timestamp)
        } for post in all_post], 200)


class WritePostView(BaseResource):
    @swag_from(WRITE_NOTICE_POST)
    @get_user_inform
    @json_required({'title': str, 'content': str})
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


class OnePostView(BaseResource):
    @swag_from(ONE_NOTICE_GET)
    @get_user_inform
    def get(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        return self.unicode_safe_json_dumps({
            'obj_id': str(post.id),
            'title': post.title,
            'author': post.author.nickname,
            'content': post.content,
            'comments': [{
                "user": data.user.nickname,
                "comment": data.comment
            } for data in post.comments],
            'tags': post.tags,
            'timestamp': str(post.timestamp)
        }, 200)

    @swag_from(ONE_NOTICE_DELETE)
    @get_user_inform
    def delete(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)
        post.delete()

        return Response('', 200)

