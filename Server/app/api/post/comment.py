from flask import Response, request, g
from flasgger import swag_from

from app.api import BaseResource, get_user_inform, json_required
from app.models.post import CommentModel, PostModel
from app.docs.post.comment import WRITE_COMMENT_POST, ONE_COMMENT_DELETE


class CommentView(BaseResource):
    @swag_from(WRITE_COMMENT_POST)
    @get_user_inform
    @json_required({'comment': str})
    def post(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        self.check_is_exist(post)

        comment_num = len(post.comments) + 1

        comment = CommentModel(
            user=g.user,
            comment=request.json['comment'],
            comment_num=comment_num
        )

        post.comments.append(comment)
        post.save()

        return Response('', 201)

    @swag_from(ONE_COMMENT_DELETE)
    @get_user_inform
    def delete(self, obj_id):
        post = PostModel.objects(id=obj_id).first()
        comment_num = int(request.args.get('comment_num'))
        self.check_is_exist(post, comment_num)

        if not len(post.comments):
            return Response('', 204)

        PostModel.objects(comments__match={"comment_num": comment_num}) \
                 .update_one(pull__comments_comment_num=comment_num)

        return '', 200
