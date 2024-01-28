import pytest
from unittest.mock import MagicMock
from src.services.user import User


def test_get_user_by_id_returns_expected_result_with_valid_id(client, app):
    user = User()
    user.id = 42
    user.email = 'jdoe@faux.com'
    user.firstName = 'Jon'
    user.lastName = 'Doe'
    user.username = 'jdoe'
    mock_user_repo = MagicMock()
    mock_user_repo.find.return_value = user
    app.container.userRepository.override(mock_user_repo)

    response = client.get('/user/42')

    assert response.status_code == 200
    assert response.json == {
        "id": 42,
        "email": "jdoe@faux.com",
        "firstName": "Jon",
        "lastName": "Doe",
        "username": "jdoe"
    }