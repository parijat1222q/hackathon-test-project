import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_crosscheck_valid():
    payload = {
        "lab_results": [{"name": "Hemoglobin", "value": 13.5}],
        "medicines": ["Paracetamol"]
    }
    response = client.post("/analyze/crosscheck", json=payload)
    assert response.status_code == 200
    assert "analyzed" in response.json()
    assert "crosscheck" in response.json()

def test_analyze_crosscheck_invalid_body():
    response = client.post("/analyze/crosscheck", data="not a json")
    assert response.status_code == 400 or response.status_code == 422

def test_analyze_crosscheck_malformed_lists():
    payload = {
        "lab_results": "notalist",
        "medicines": 123
    }
    response = client.post("/analyze/crosscheck", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "lab_results and medicines must be lists."
