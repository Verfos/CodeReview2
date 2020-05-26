from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from config import *


class User(UserMixin, db.Model):
    """Класс позьзователя для работы с сайтом.

    Хранит данные о пользователе и хранит информацию
    о состоянии пользователя на сайте
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_answers = db.Column(db.Integer)
    question_order = db.Column(db.Integer)

    def __init__(self, number_of_answers, question_order):
        self.number_of_answers = number_of_answers
        self.question_order = question_order


class UserTest(db.Model):
    """Класс  для хранения информации о тестировании пользователя.

    Хранит данные о текущем прогрессе позьзователя
    """
    id = db.Column(db.Integer, primary_key=True)
    current_answer = db.Column(db.Integer)
    logics = db.Column(db.Integer)
    ethics = db.Column(db.Integer)
    sensitive = db.Column(db.Integer)
    intuition = db.Column(db.Integer)

    def __init__(self, current_answer, logics, ethics, sensitive, intuition):
        self.current_answer = current_answer
        self.logics = logics
        self.ethics = ethics
        self.sensitive = sensitive
        self.intuition = intuition


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_of_answer = db.Column(db.Integer)
    where_plus = db.Column(db.Integer)
    answer_text = db.Column(db.String(50))
    qu_id = db.Column(db.Integer)

    def __init__(self, order_of_answer, where_plus, answer_text, qu_id):
        self.order_of_answer = order_of_answer
        self.where_plus = where_plus
        self.answer_text = answer_text
        self.qu_id = qu_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])
