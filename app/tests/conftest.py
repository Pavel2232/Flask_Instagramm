import pytest
from app.run import app


@pytest.fixture(scope='session')
def client():
    return app.test_client()


