from fast_zero.models import User


def test_create_user():
    user = User(
        username="teste", email="teste@gmail.com", password="minha_senha"
    )

    assert user.username == "teste"
