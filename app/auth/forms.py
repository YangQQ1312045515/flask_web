from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64),Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住登陆')
    submit = SubmitField('登陆')

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64),Email()])
    username = StringField('用户名', validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters,''numbers, dots or underscores')])
    password = PasswordField('密码', validators=[Required(), EqualTo('password2',message='Passwords must match.')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在.')

class ChangePasswordForm(Form):
    username = StringField('新用户名')
    new_password1 = StringField('新密码',validators=[Required(), EqualTo('new_password2',message='Password must match')])
    new_password2 = StringField('确认密码',validators=[Required()])
    submit = SubmitField('提交')
