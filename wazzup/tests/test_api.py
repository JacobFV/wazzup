import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Communications Assistant Backend"}

def test_authenticate_notion():
    credentials = {"api_key": "test_api_key"}
    response = client.post("/data-ingestion/notion/authenticate", json=credentials)
    assert response.status_code == 200
    assert response.json() == {"message": "Notion authentication successful"}

def test_fetch_notion_data():
    response = client.post("/data-ingestion/notion/fetch-data")
    assert response.status_code == 200
    assert "data" in response.json()

# Write similar tests for other API endpoints

