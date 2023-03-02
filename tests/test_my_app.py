from unittest import mock

from pytest import fixture

from sanic_testing.reusable import ReusableClient

from my_app import app


@fixture
def client():
    yield ReusableClient(app)


def test_home(client):
    with client:
        _, response = client.get("/")
        assert response.status_code == 418
        assert response.text == "I'm a teapot"
