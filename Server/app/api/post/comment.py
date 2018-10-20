from flask import Response, request, g

from app.api import BaseResource, get_user_inform, json_required
from app.models.post import CommentModel, PostModel


class CommentView(BaseResource):
    @get_user_inform
    @json_required({'comment': str})
    def post(self, obj_id, comment_num):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post, comment_num)

        new_comment_num = len(post.comments) + 1

        comment = CommentModel(
            user=g.user,
            comment=request.json['comment'],
            comment_num=new_comment_num
        )

        post.comments.append(comment)
        post.save()

        return Response('', 201)

    @get_user_inform
    def delete(self, obj_id, comment_num):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post, comment_num)

        if not len(post.comments):
            return Response('', 204)

        comment = PostModel.objects(comment__match={"comment_num": comment_num}).first()
        comment.delete()

        return Response('', 200)
