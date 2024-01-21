"""
Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет выведено "Привет, {имя}!".

"""

from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = b'cf1c989b37b0a2c850bc71d53ab8a113cefd5682d0aa4f9bcd631ecbe02f30e0'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_name = request.form.get('name')
        flash(f'Привет, {user_name}')
        return render_template('responce.html')

if __name__ == '__main__':
    app.run(debug=True)