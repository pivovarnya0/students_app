
from app import app

def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"StudentSpace" in response.data

def test_courses_page():
    response = app.test_client().get("/courses")
    assert response.status_code == 200
    assert "DevOps".encode() in response.data

def test_about_page():
    response = app.test_client().get("/about")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_api_courses():
    response = app.test_client().get("/api/courses")
    assert response.status_code == 200
    data = response.get_json()
    assert "courses" in data
    assert len(data["courses"]) == 5
    assert data["courses"][0]["name"] == "DevOps инженерия"
