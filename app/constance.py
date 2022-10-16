from post.dao.comment_dao import CommentDAO, COMMENT_PATH
from post.dao.post_dao import DATA_PATH, PostDAO

"""Готовый класс пост_дао"""
post_dao = PostDAO(DATA_PATH)
"""готовый класс коммент_дао"""
comment_dao = CommentDAO(COMMENT_PATH)
