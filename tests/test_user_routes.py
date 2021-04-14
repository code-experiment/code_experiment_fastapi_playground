import requests


def test_get_user():

    # Arrange
    url = 'http://localhost:8000/get-user/1'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 1 == body['id']
    assert 1 is body['id']


def test_get_user_raises_user_not_found():

    # Arrange
    url = 'http://localhost:8000/get-user/1120398'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert 'User Not Found' in body['detail']
