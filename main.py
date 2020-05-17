from views import *
import pytest


def test_login():
    client = app.test_client()
    rv = client.post('login', data=dict(username='example', passwaord='example'), follow_redirects=True)
    assert 60 == rv.data[0]


def test_testing():
    client = app.test_client()
    rv = client.post('login', data=dict(username='example', password='example'))
    assert rv.status_code == 200

if __name__ == '__main__':

    app.run(debug=False, host=arg.host, port=arg.port)