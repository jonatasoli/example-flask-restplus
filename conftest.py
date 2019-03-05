import pytest
from flask import Flask

from core.factories.app_factory import create_app
from ext.db import db
import config


@pytest.fixture(scope='session')
def app():
    config.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    config.SQLALCHEMY_POOL_SIZE = 5
    config.SECRET_KEY = 'Test Key'
    app_ = create_app(config)
    app_.testing = True
    with app_.test_request_context() as _:
        yield app_


@pytest.fixture(scope='module')
def db_session(app):
    db.create_all()
    yield db.session
    db.drop_all()


@pytest.fixture
def client(app: Flask):
    with app.test_client() as c:
        yield c


@pytest.fixture
def flask_session(client):
    with client.session_transaction() as sess:
        yield sess

