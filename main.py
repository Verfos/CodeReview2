from views import app, args, login_user, User, update_answer, UserTest
import pytest


def test_login():
    client = app.test_client()
    client_respone = client.post('login', data=dict(username='example', passwaord='example'), follow_redirects=True)
    assert 60 == client_respone.data[0]


def test_testing():
    client = app.test_client()
    response = client.post('login', data=dict(username='example', password='example'))
    assert response.status_code == 200


def test_new_user():
    new_user = User(username='newuser', email='something@gmail.com', password='somepass')
    assert new_user.email == 'something@gmail.com'
    assert new_user.password != 'dwadaw'


def test_logout():
    client = app.test_client()
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert response.data[1] == 33
    assert response.data[2] == 68


def test_update_answer():
    user = UserTest(1, 0, 0, 0, 0)
    update_answer(user, 1)
    assert user.logics == 1
    assert user.ethics == 0
    assert user.sensitive == 0
    assert user.intuition == 0
    
    for i in range (10):
        update_answer(user, 1)
    assert user.current_answer == 12
    
    for i in range (1,8,2):
        print(i)
        update_answer(user, i)
    
    assert user.logics == 12
    assert user.ethics == 1
    assert user.sensitive == 1
    assert user.intuition == 1
    

if __name__ == '__main__':
    app.run(debug=False, host=args.host, port=args.port)
