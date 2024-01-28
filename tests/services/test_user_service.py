import pytest
from unittest.mock import MagicMock
from src.services.user import User
from src.services.user_service import UserService


def test_get_user_returns_dict_with_all_vals_set():
    user = User()
    user.id = 42
    user.email = 'jdoe@fake.faux'
    user.firstName = 'Jon'
    user.lastName = 'Doe'
    user.username = 'jdoe'
    mock_user_repo = MagicMock()
    mock_user_repo.find.return_value = user
    svc = UserService(user_repository=mock_user_repo)

    result = svc.get_user(42)

    assert result is not None
    assert result == {
        "id": 42,
        "email": "jdoe@fake.faux",
        "firstName": "Jon",
        "lastName": "Doe",
        "username": "jdoe"
    }


def test_get_user_returns_none_when_user_doesnt_exist():
    mock_user_repo = MagicMock()
    mock_user_repo.find.return_value = None
    svc = UserService(user_repository=mock_user_repo)

    result = svc.get_user(42)
    
    assert result is None
