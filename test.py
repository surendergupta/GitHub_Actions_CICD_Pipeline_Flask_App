from app import app

def test_hello_world():
    response = app.test_client().get('/')
    print(response.status_code)
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my first API call!'
    