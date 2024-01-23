from src.app_factory import create_app


def test_conf():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_healthcheck(client):
    response = client.get('healthcheck')
    assert response.data == b'alive'
    