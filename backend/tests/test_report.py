import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_report_valid():
    response = client.get("/report/12345")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"

def test_report_invalid_id():
    response = client.get("/report/")
    assert response.status_code == 400
    assert response.json()["detail"] == "Report id must be a non-empty string."
