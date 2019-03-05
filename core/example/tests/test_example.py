import pytest
from core.example.models import ToDo
from ext.db import db

"""
@pytest.fixture(scope='module')
def new_task(init_db):
    first_task = ToDo(
        task='Todo 1',
        description='My first Todo'
    )
    db.session.add(first_task)
    db.session.commit()


def test_new_task(new_task):
    assert new_task.id == 1
    assert new_task.task == 'Todo 1'
    assert new_task.description == 'My first Todo'
    assert new_task.activate is True
"""


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_get_all_todo(client):
    response = client.get('/example/todo/')
    assert response.status_code == 201


def test_create_task(client):
    response = client.post('/example/todo', json={
        'task': 'Todo 1',
        'description': 'My fist task'
    })
    json_data = response.get_json()
    assert response.status_code == 200

"""
def test_get_all_todo(client):
    response = client.get('/example/todo')
    assert response.status_code == 200
    
    assert response.json == {
        'id': 1,
        'task': 'Todo 1',
        'description': 'My first Todo',
        'activate': True
    }
"""
