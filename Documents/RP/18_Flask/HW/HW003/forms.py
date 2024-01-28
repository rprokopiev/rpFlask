from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    user_email = StringField('Email', validators=[DataRequired(), Email(message='Wrong')])
    user_password = PasswordField('Пароль', validators=[DataRequired()])