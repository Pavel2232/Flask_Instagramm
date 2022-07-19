from app.constance import post_dao
from app.run import app

key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}


class TestAPI:
    """Тест основной страницы"""

    def test_index(self, client):
        response = app.test_client().get('/')
        assert response.status_code != 500, f"Статус - код{response.status_code}"

    def test_api_all(self, client):
        """Проверка api постов"""
        response = app.test_client().get('/api/posts')
        assert response.status_code == 200, f"Статус - код{response.status_code} запроса постов {response.json}"
        assert isinstance(response.json, list), type(response.json)
        assert set(post_dao.get_data()[
                       0].keys()) == key_data, f"{set(post_dao.get_all()[1].key())} получаем , а надо {key_data}"

    def test_api_queri(self, client):
        """Проверка api с обращением к 1 посту"""
        response = app.test_client().get("/api/posts/1")
        assert response.status_code == 200
        assert isinstance(response.json, dict), type(response.json)
        assert set(post_dao.get_data()[
                       0].keys()) == key_data, f"{set(post_dao.get_all()[1].key())} получаем , а надо {key_data}"
