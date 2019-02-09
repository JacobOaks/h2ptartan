from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Start(FlaskForm):
    submit = SubmitField('START')
