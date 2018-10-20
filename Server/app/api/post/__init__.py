from flask import Blueprint
from flask_restful import Api


blueprint = Blueprint('post', __name__)
api = Api(blueprint)
api.prefix = '/post'


from .post import ShowAllPostView, WritePostView, OnePostView
api.add_resource(ShowAllPostView, '')
api.add_resource(WritePostView, '')
api.add_resource(OnePostView, '/<obj_id>')

from .comment import CommentView
api.add_resource(CommentView, '/<obj_id>/comment/<comment_num>')
