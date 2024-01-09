def test_register(fastapi_client):
    response = fastapi_client.post("/auth/register", json={
        "email": "string111121",
        "password": "string1111121",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string1111121",
    })

    assert response.status_code == 201
