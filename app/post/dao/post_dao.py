import json
from app.post.dao.post import Post
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError
from app.config import DATA_DIR

DATA_PATH = DATA_DIR.joinpath("data.json")


class PostDAO:

    def __init__(self, path):
        self.path = DATA_PATH

    def get_data(self):
        """Форматирование json """
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                post_data = json.load(f)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла{self.path}")
        return post_data

    def load_data(self) -> list[Post]:

        posts = []
        for post in self.get_data():
            posts.append(Post(
                post["poster_name"],
                post["poster_avatar"],
                post["pic"],
                post["content"],
                post["views_count"],
                post["likes_count"],
                post["pk"]
            ))
        return posts

    def get_all(self) -> list[Post]:
        """Получить все Посты"""
        return self.load_data()

    def get_posts_all(self, user_name) -> list[Post]:
        """Подробно 1 пост"""
        if type(user_name) != str:
            raise TypeError("user_name не  str")

        users_posts = []
        post_lower = str(user_name).lower()
        for post in self.get_all():
            post_poster_name = post.poster_name.lower()
            if post_lower in post_poster_name:
                users_posts.append(post)
        return users_posts

    def search_for_posts(self, query) -> list[Post]:
        """Поиск поста по совпадению"""

        if type(query) != str:
            raise TypeError("query не  str")

        list_post = []
        post_lower = str(query).lower()

        for post in self.get_all():
            post_content = post.content.lower()
            if post_lower in post_content:
                list_post.append(post)
        return list_post

    def get_post_by_pk(self, pk):
        """Получаем пост по номеру"""
        for post in self.get_all():
            if post.pk == pk:
                return post
        return None
