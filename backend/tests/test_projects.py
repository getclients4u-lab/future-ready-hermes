import pytest


@pytest.mark.asyncio
async def test_create_project(client):
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={"email": "project@example.com", "password": "testpass123"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "project@example.com", "password": "testpass123"},
    )
    token = login.json()["access_token"]

    response = await client.post(
        "/api/v1/projects/?name=Test+Project&description=A+test+project",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Project"


@pytest.mark.asyncio
async def test_list_projects_requires_auth(client):
    response = await client.get("/api/v1/projects/")
    assert response.status_code == 403
