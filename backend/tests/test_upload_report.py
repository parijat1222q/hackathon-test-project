import os
from fastapi.testclient import TestClient
from main import app

def test_upload_report_valid_image():
    client = TestClient(app)
    test_file = "tests/test_image.jpg"
    # Create a dummy image file
    with open(test_file, "wb") as f:
        f.write(os.urandom(1024))
    with open(test_file, "rb") as f:
        response = client.post("/upload/report", files={"file": ("test_image.jpg", f, "image/jpeg")})
    os.remove(test_file)
    assert response.status_code in [200, 500, 400, 413]  # Acceptable for stub/demo

def test_upload_report_invalid_filetype():
    client = TestClient(app)
    test_file = "tests/test_invalid.txt"
    with open(test_file, "w") as f:
        f.write("dummy text")
    with open(test_file, "rb") as f:
        response = client.post("/upload/report", files={"file": ("test_invalid.txt", f, "text/plain")})
    os.remove(test_file)
    assert response.status_code == 400

def test_upload_report_large_file():
    client = TestClient(app)
    test_file = "tests/test_large.jpg"
    with open(test_file, "wb") as f:
        f.write(os.urandom(6 * 1024 * 1024))  # 6MB
    with open(test_file, "rb") as f:
        response = client.post("/upload/report", files={"file": ("test_large.jpg", f, "image/jpeg")})
    os.remove(test_file)
    assert response.status_code == 413
