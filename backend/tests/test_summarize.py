import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize_valid():
    payload = {"text": "Patient has fever and cough. Paracetamol prescribed."}
    response = client.post("/summarize", json=payload)
    assert response.status_code == 200
    assert "summary" in response.json()
    assert "keywords" in response.json()

def test_summarize_invalid_body():
    response = client.post("/summarize", data="not a json")
    assert response.status_code == 400 or response.status_code == 422

def test_summarize_invalid_text():
    payload = {"text": ""}
    response = client.post("/summarize", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Text must be a non-empty string."
