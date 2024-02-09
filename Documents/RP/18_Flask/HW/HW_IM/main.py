'''
Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей. 
Пользователь должен иметь следующие поля: 
○ ID (автоматически генерируется при создании пользователя) 
○ Имя (строка, не менее 2 символов) 
○ Фамилия (строка, не менее 2 символов) 
○ Дата рождения (строка в формате "YYYY-MM-DD") 
○ Email (строка, валидный email) 
○ Адрес (строка, не менее 5 символов)

API должен поддерживать следующие операции: 
- Добавление пользователя в базу данных 
- Получение списка всех пользователей в базе данных 
- Получение пользователя по ID Обновление пользователя по ID 
- Удаление пользователя по ID 
- Приложение должно использовать базу данных SQLite3 для хранения пользователей
'''
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


app = FastAPI()


con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, 
                last_name TEXT, 
                date_of_birth TEXT, 
                email TEXT, 
                address TEXT
            )
''')


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    address: str


@app.post('/users')
def create_user(user: User):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users (first_name, last_name, date_of_birth, email, address) VALUES (?, ?, ?, ?, ?)', 
                (user.first_name, user.last_name, user.date_of_birth, user.email, user.address))
    con.commit()
    con.close()
    return {'message': 'User created successfully'}


@app.get('/users')
def get_all_users():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    con.close()
    return {'users': users}


@app.get('/users/{user_id}')
def get_user(user_id: int):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cur.fetchone()
    con.close()
    return {'user': user}


@app.put('/users/{user_id}')
def update_user(user_id: int, user: User):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('UPDATE users SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, address = ? WHERE id = ?', 
                (user.first_name, user.last_name, user.date_of_birth, user.email, user.address, user_id))
    con.commit()
    con.close()
    return {'message': 'User updated successfully'}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    con.commit()
    con.close()
    return {'message': 'User deleted successfully'}