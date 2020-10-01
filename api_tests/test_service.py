import json

from pytest import fixture, mark


@fixture
def service():
    from api_tests.service import Service
    return Service()


@fixture
def test_payload():
    with open('schemas/test_payload.json') as json_:
        payload = json.load(json_)
        return payload


def test_create_user(service, test_payload):
    r = service.create_user(test_payload)
    assert r.status_code == 201, f"failed to create user, expected s.code 201, " \
                                 f"instead got: {r.status_code} with message {r.text}"


@mark.parametrize('field_name', ['userId', 'id', 'title', 'completed'])
def test_get_user_by_id(service, test_payload, field_name):
    r = service.get_user_by_id('1')
    assert r.status_code == 200, f"failed to get user by id: '1', expected s.code 200, " \
                                 f"instead got: {r.status_code} with message {r.text}"
    assert r.json()[field_name] == test_payload[field_name], \
        f"failed to get expected value in field: {field_name}, expected: {test_payload[field_name]}, " \
        f"instead got: {r.json()[field_name]}"


def test_get_users(service):
    r = service.get_users()
    assert r.status_code == 200, f"failed to get user by id: '1', expected s.code 200, " \
                                 f"instead got: {r.status_code} with message {r.text}"
    users = r.json()
    for user in users:
        assert [i for i in user.keys()] == ['userId', 'id', 'title', 'completed'], \
            f"failed to get expected keys in users resp payload, expected:" \
            f" 'userId', 'id', 'title', 'completed', instead got: {[i for i in user.keys()]}"
