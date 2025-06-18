from app import app

def test_home_status():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_content():
    client = app.test_client()
    response = client.get('/')
    assert b"Hello, CI/CD World!" in response.data  # <- fixed line

def test_home_route_exists():
    client = app.test_client()
    response = client.get('/')
    assert response is not None

def test_home_returns_string():
    client = app.test_client()
    response = client.get('/')
    assert isinstance(response.data, bytes)
