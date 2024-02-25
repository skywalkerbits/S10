import pytest
from app import create_app, db, config_dict


@pytest.fixture()
def app():
    config_dict["development"].SQLALCHEMY_DATABASE_URI = "sqlite://"

    app = create_app("development")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_all_data(client):
    assert len(client.get("/data").json) == 0


def test_insert_data(client):
    request_body = {
        "name": "new_data"
    }

    response = client.post("data", json=request_body)

    assert response.status_code == 200
    assert len(client.get("/data").json) == 1


def test_insert_duplicated_data(client):
    request_body = {"name": "new_data"}

    client.post("data", json=request_body)
    response = client.post("data", json=request_body)

    assert response.status_code == 409
    assert len(client.get("/data").json) == 1


def test_delete_data(client):
    request_body = {"name": "new_data"}

    client.post("/data", json=request_body)
    response = client.delete("/data/1")

    assert response.status_code == 200
    assert len(client.get("/data").json) == 0


def test_delete_non_existing_data(client):
    response = client.delete("/data/9999999")
    assert response.status_code == 404
    assert len(client.get("/data").json) == 0
