# encoding: utf-8
import pytest

from tests import utils

from app import create_app


@pytest.yield_fixture(scope="session")
def flask_app():
    app = create_app(config_name="test")

    with app.app_context():
        yield app



@pytest.fixture(scope="session")
def flask_app_client(flask_app):
    flask_app.response_class = utils.JSONResponse
    return flask_app.test_client()
