"""
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""

from flask import Flask, render_template, request
from models import db, User
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


app.config['SECRET_KEY'] = b'08cd834fdc836240ba43d257962ab15a23ba5ef98f1ab57bb070fe85bd0fb7f7'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/login/', methods=['GET', 'POST'])
def login():
    db.create_all()
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        fn = form.first_name.data
        ln = form.last_name.data
        em = form.user_email.data
        pss = form.user_password.data
        new_user = User(first_name=fn, last_name=ln, email=em, password=pss)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

