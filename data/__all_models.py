import sqlalchemy
from .db_session import SqlAlchemyBase
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

sqlalchemy.Table(
    'tags_to_memes',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('tag', sqlalchemy.Integer, sqlalchemy.ForeignKey('tags.id')),
    sqlalchemy.Column('meme', sqlalchemy.Integer, sqlalchemy.ForeignKey('memes.id'))
)

sqlalchemy.Table(
    'likes',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('meme', sqlalchemy.Integer, sqlalchemy.ForeignKey('memes.id'))
)

from . import memes
from . import tags
from . import users


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    rep_password = PasswordField('Повтор пароля', validators=[DataRequired()])
    alias = StringField('Псевдоним', validators=[DataRequired()])
    bdate = DateField("Дата рождения", validators=(validators.Optional(),))
    about = StringField("Немного о себе, если хотите))")
    avatar = FileField("Изображение профиля", validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Зарегистрироваться")


