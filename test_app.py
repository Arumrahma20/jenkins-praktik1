from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 20
    assert b"Hello from Jenkins Multibranch Pipeline!" in response.data