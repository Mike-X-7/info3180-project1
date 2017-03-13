from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import  PasswordField, TextField, TextAreaField, SelectField
from wtforms.validators import Required,InputRequired ,NumberRange, ValidationError

class LoginForm(FlaskForm):
    firstname = TextField('Firstname', validators=[Required("Please enter your Firstname.")])
    lastname = TextField('Lastname', validators=[Required("Please enter your Lastname.")])
    username = TextField('Username', validators=[Required("Please enter your Lastname.")])
    age = TextField('Age', validators=[Required(),NumberRange(min=5, max=105)])
    gender = SelectField('Gender', choices=[('man', 'Male'), ('woman', 'Female')])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    image = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'gif','png'], 'Images only!')])
    