from app.constance import post_dao
from app.post.dao.post import Post
import pytest

# Задаем, какие ключи ожидаем получать у постов
key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}


class TestPostDao:

    @pytest.fixture
    def post_dao(self):
        return post_dao

    def test_get_all_types(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_all()
        assert type(posts) == list, "возвращается не список"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "неверный список Класса"

    def test_get_by_id(self, post_dao):
        """ Проверяем правильность pk  кандидатов возвращаются при запросе"""
        posts = post_dao.get_all()

        correct_pks = {1, 2, 3, 4, 5, 6, 7, 8}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Не совпадает получение pk"

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None, "Нет такого пользолвателя"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, f"Неыерный ключь пк для запроса пк"

    def test_search_is_correct(self, post_dao):
        """Проверка поиска поста"""
        posts = post_dao.search_for_posts("ага")
        assert type(posts) == list, "Вернулся не список"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "Некорректный тип 1 поста"

    def test_search_is_correct_not_found(self, post_dao):
        """Проверка что поста такого нет"""
        posts = post_dao.search_for_posts("9999999999999")
        assert posts == [], "Ничего не найдено"

    @pytest.mark.parametrize("s,expected_pks", [
        ("Ага", {1}),
    ])
    def test_search_is_coerrect_result(self, post_dao, s, expected_pks):
        """Проверка совпадения текста с постом"""
        posts = post_dao.search_for_posts(s)
        pks = set([post.pk for post in posts[:1]])
        assert pks == expected_pks, f"Не найден результат для {s}"
