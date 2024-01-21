"""
Создать страницу, на которой будет форма для ввода имени и электронной почты
При отправке которой будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти" 
При нажатии на кнопку будет удален cookie файл с данными пользователя 
и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        check = request.cookies.get('username')
        if check != None:
            response = make_response(render_template('index.html'))
            response.delete_cookie('username')
            response.delete_cookie('email')
            return response
        else:
            return render_template('index.html')
     
    else:
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        context = {
            'user_name': user_name,
            'user_email': user_email
        }
        response = make_response(render_template('responce.html', **context))
        response.set_cookie('username', user_name)
        response.set_cookie('email', user_email)
        return response

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('username')
   return '<h1>welcome ' + f'{name}' + '</h1>'

app.route('/delCookie/')
def delCookie():
    # if response != '':
    #     response.set_cookie('username', 0)
    #     response.set_cookie('email', 0)
    return redirect(url_for('index'), 301)

if __name__ == '__main__':
    app.run(debug=True)