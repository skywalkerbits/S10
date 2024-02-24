import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app("development")
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_all_data(client):
    assert len(client.get("/data").json) == 1
