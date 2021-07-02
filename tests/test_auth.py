import pytest


@pytest.mark.auth
def test_login(test_db_session, create_single_user, credentials, client):
    # Arrange
    url = '/login'
    payload = {
        "username": credentials.get('username'),
        "password": credentials.get('password')
    }

    # Act
    response = client.post(url, data=payload)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert "access_token" in body
    assert body["token_type"] == "bearer"


@pytest.mark.auth
def test_login_with_invalid_user_raises_error(client):
    # Arrange
    url = '/login'
    payload = {
        "username": "WRONG_USERNAME",
        "password": "WRONG_PASSWORD"
    }

    # Act
    response = client.post(url, data=payload)
    body = response.json()

    # Assert
    assert response.status_code == 401
    assert body["detail"] == "Incorrect username or password."


@pytest.mark.auth
def test_login_with_wrong_password_raises_error(create_single_user, client):
    # Arrange
    url = '/login'
    payload = {
        "username": create_single_user.username,
        "password": "WRONG_PASSWORD"
    }

    # Act
    response = client.post(url, data=payload)
    body = response.json()

    # Assert
    assert response.status_code == 401
    assert body["detail"] == "Incorrect username or password."
