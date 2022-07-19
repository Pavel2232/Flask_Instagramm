from app.post.dao.comment import Comment
import json
from app.config import DATA_DIR

COMMENT_PATH = DATA_DIR.joinpath('comments.json')


class CommentDAO:
    def __init__(self, path):
        self.path = COMMENT_PATH

    def load_data(self) -> list[Comment]:
        """Получение списка"""
        with open(self.path, "r", encoding="utf-8") as f:
            comments_data = json.load(f)
            comments = []
            for comment in comments_data:
                comments.append(Comment(
                    comment["post_id"],
                    comment["commenter_name"],
                    comment["comment"],
                    comment["pk"],
                ))
        return comments

    def get_comments_by_post_id(self, post_id) -> list[Comment]:
        """Все комментарии к 1 посту"""
        posts = self.load_data()
        comments_post = []
        for post in posts:
            if post.post_id == post_id:
                comments_post.append(post)
        return comments_post
