"""
Создать страницу, на которой будет форма для ввода имени и электронной почты
При отправке которой будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти" 
При нажатии на кнопку будет удален cookie файл с данными пользователя 
и произведено перенаправление на страницу ввода имени и электронной почты.

"""

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        response = make_response(f'Cookie установлен')
        response.set_cookie('username', user_name)
        response.set_cookie('email', user_email)
        context = {
            'user_name': user_name,
            'user_email': user_email
        }
    # return 'response'
    return render_template('responce.html', **context)

if __name__ == '__main__':
    app.run(debug=True)