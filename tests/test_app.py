from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_return_ok_and_hello_world(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "mytest",
            "email": "usertest@example.com",
            "password": "anypass",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "mytest",
        "email": "usertest@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")
    assert response.json() == {"users": [user_schema]}


def test_update_user(client, user):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "testusername2",
            "email": "usertest@example.com",
            "id": 1,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "testusername2",
        "email": "usertest@example.com",
        "id": 1,
    }


def test_delete_user(client, user):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
