from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Signup')

class SpellSearchForm(FlaskForm):
    name = StringField('Spell Name')
    level = StringField('Level')
    description = StringField('Part of description')
    actions = StringField('Number/type of action')
    traits = StringField('Search tags')
    range = StringField('Range')
    duration = StringField('Duration')
    target = StringField('Target')
    tradition = StringField('Tradition')
    submit = SubmitField('Search')