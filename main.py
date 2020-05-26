from views import app, args
import pytest


def test_login():
    client = app.test_client()
    client_respone = client.post('login', data=dict(username='example', passwaord='example'), follow_redirects=True)
    assert 60 == client_respone.data[0]


def test_testing():
    client = app.test_client()
    rv = client.post('login', data=dict(username='example', password='example'))
    assert rv.status_code == 200


if __name__ == '__main__':
    app.run(debug=False, host=args.host, port=args.port)
