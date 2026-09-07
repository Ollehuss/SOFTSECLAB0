from src.api import app

def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.mimetype == "application/json"
    assert response.get_json() == {"message": "Hello, World!"}

def test_hello_one_l():
    client = app.test_client()
    response = client.get("/helo")
    assert response.status_code == 404
    