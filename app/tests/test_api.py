import pytest
from app.run import app
from app.post.dao.post_dao import PostDAO,DATA_PATH


def test_api_all():
    response = app.test_client().get('/api/posts',  follow_redirects=True)
    assert response.status_code == 200, "Статус - код запроса постов не верный"
    assert response.data == PostDAO(DATA_PATH).get_all()
    assert type(response) == list, "Возвращается не список"
    assert PostDAO(DATA_PATH).get_all() in response.set_cookie(),"Неправильный ключь"





