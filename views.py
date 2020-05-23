from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from enum import Enum


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            return render_template('login2.html')
        login_user(user, remember=form.remember.data)
        return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        new_user1 = UserTest(1, 0, 0, 0, 0)
        db.session.add(new_user1)
        db.session.commit()

        return render_template('signup2.html')

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def update_answer(current_user_info, answer):
    if answer == 1:
        current_user_info.logics += 1
    elif answer == 2:
        current_user_info.logics -= 1
    elif answer == 3:
        current_user_info.ethics += 1
    elif answer == 4:
        current_user_info.ethics -= 1
    elif answer == 5:
        current_user_info.sensitive += 1
    elif answer == 6:
        current_user_info.sensitive -= 1
    elif answer == 7:
        current_user_info.intuition += 1
    elif answer == 8:
        current_user_info.intuition += 1
    current_user_info.current_answer += 1


def render_answer(current_user, new_number_of_question, new_all_answers):
    if new_number_of_question == 2:
        return render_template('testing.html', name=current_user.username, result=1,
                               answer1=new_all_answers[0].answer_text, answer2=new_all_answers[1].answer_text)
    elif new_number_of_question == 4:
        return render_template('testing1.html', name=current_user.username, result=1,
                               answer1=new_all_answers[0].answer_text, answer2=new_all_answers[1].answer_text,
                               answer3=new_all_answers[1].answer_text, answer4=new_all_answers[1].answer_text)
    else:
        return redirect(url_for('dashboard'))


def update_user(answer, question_order, current_question):
    current_user_info = db.session.query(UserTest).get(current_user.id)
    update_answer(current_user_info, answer)
    db.session.query(User).filter_by(id=current_user.username).update({User.username: User.username})
    order = question_order.current_answer
    new_current_question = db.session.query(Question).filter_by(question_order=order).first_or_404()
    new_number_of_question = current_question.number_of_answers
    new_all_answers = db.session.query(Answer).filter_by(qu_id=current_question.id).all()
    db.session.commit()
    new_render = render_answer(current_user, new_number_of_question, new_all_answers)
    return new_render


@app.route('/testing', methods=['GET', 'POST'])
@login_required
def testing():
    current_user_info = db.session.query(UserTest).filter_by(id=current_user.id).one()
    if current_user_info.current_answer >= 20:
        return render_template('testing3.html')
    order = current_user_info.current_answer
    current_question = db.session.query(Question).filter_by(question_order=order).first_or_404()
    number_of_question = current_question.number_of_answers
    all_answers = db.session.query(Answer).filter_by(qu_id=current_question.id).all()
    answer = current_user.username
    if request.method == 'POST':
        chosen_answer = request.form['submit']
        if chosen_answer == 'profile1':
            updated_answer = all_answers[0].where_plus
        elif chosen_answer == 'profile2':
            updated_answer = all_answers[1].where_plus
        elif chosen_answer == 'profile3':
            updated_answer = all_answers[2].where_plus
        elif chosen_answer == 'profile4':
            updated_answer = all_answers[3].where_plus
        update_user(updated_answer, current_user_info, current_question)
    new_render = render_answer(current_user, number_of_question, all_answers)
    return new_render


@app.route('/show_your_type', methods=['GET', 'POST'])
@login_required
def show_your_type():
    current_user_info = db.session.query(UserTest).filter_by(id=current_user.id).one()
    first = "Рациоанльный" if current_user_info.logics > 0 else "Иррациональный"
    second = "Этический" if current_user_info.ethics > 0 else "Сенсорный"
    third = "Логический" if current_user_info.sensitive > 0 else "Интуитивный"
    fourth = "Экстроверт" if current_user_info.intuition > 0 else "Интроверт"
    user_type = "Ваш тип:" + " " + first + " " + second + " " + third + " " + fourth
    if current_user_info.current_answer >= 20:
        return render_template('show_your_type.html', out=user_type)
    return render_template('show_your_type.html', out="Вы ещё не прошли тест")