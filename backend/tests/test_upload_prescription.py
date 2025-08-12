import os
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_prescription_valid_image():
    file_path = "tests/data/valid_prescription.jpg"
    if not os.path.exists(file_path):
        pytest.skip("Test image not found")
    with open(file_path, "rb") as f:
        response = client.post("/upload/prescription", files={"file": ("valid_prescription.jpg", f, "image/jpeg")})
    assert response.status_code == 200
    assert "medicines" in response.json()

def test_upload_prescription_invalid_type():
    file_path = "tests/data/invalid.txt"
    if not os.path.exists(file_path):
        pytest.skip("Test file not found")
    with open(file_path, "rb") as f:
        response = client.post("/upload/prescription", files={"file": ("invalid.txt", f, "text/plain")})
    assert response.status_code == 400
    assert response.json()["detail"] == "Only PDF and image files are allowed."

def test_upload_prescription_large_file():
    file_path = "tests/data/large_prescription.jpg"
    if not os.path.exists(file_path):
        pytest.skip("Large test image not found")
    with open(file_path, "rb") as f:
        response = client.post("/upload/prescription", files={"file": ("large_prescription.jpg", f, "image/jpeg")})
    assert response.status_code == 413
    assert response.json()["detail"] == "File size exceeds 5MB limit."
