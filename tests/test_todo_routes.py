import pytest


@pytest.mark.todos
def test_create_new_todo(login, client):
    # Arrange
    url = '/create-todo'
    payload = {
        "title": "Buy Milk",
        "complete": False
    }
    headers = {
        "Authorization": f"Bearer {login['access_token']}"
    }

    # Act
    response = client.post(url, headers=headers, json=payload)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body['title'] == 'Buy Milk'
    assert body['complete'] == False
    assert body['id'] == 1
    assert body['owner_id'] == 1


@pytest.mark.todos
def test_create_new_todo_raises_not_authenticated(client):
    # Arrange
    url = '/create-todo'
    payload = {
        "title": "Buy Milk",
        "complete": False
    }

    # Act
    response = client.post(url, json=payload)
    body = response.json()

    # Assert
    assert response.status_code == 401
    assert body["detail"] == "Not authenticated"


@pytest.mark.todos
def test_get_user_todos_has_todos(login, client, create_single_todo):
    # Arrange
    url = "/get-todos"
    headers = {
        "Authorization": f"Bearer {login['access_token']}"
    }

    # Act
    response = client.get(url, headers=headers)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body['todos'], list)
    assert len(body['todos']) >= 1