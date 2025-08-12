import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_research_valid():
    response = client.get("/research", params={"term": "diabetes"})
    assert response.status_code == 200
    assert "links" in response.json()

def test_research_invalid_term():
    response = client.get("/research", params={"term": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Search term must be a non-empty string."
