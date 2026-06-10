import pytest


@pytest.mark.asyncio
async def test_register_user(client):
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "securepassword123",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test User"
    assert "id" in data


@pytest.mark.asyncio
async def test_register_duplicate_email(client):
    payload = {
        "email": "dup@example.com",
        "password": "securepassword123",
    }
    await client.post("/api/v1/auth/register", json=payload)
    response = await client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_login_success(client):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "login@example.com", "password": "testpass123"},
    )
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "login@example.com", "password": "testpass123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials(client):
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "bad@example.com", "password": "wrong"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_me_unauthorized(client):
    response = await client.get("/api/v1/auth/me")
    assert response.status_code == 403
