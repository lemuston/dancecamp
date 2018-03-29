from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField

class DanceclassForm(FlaskForm):
    name = StringField("name"), [validators.Length(min=2)]
    duration = IntegerField("duration")
 
    class Meta:
        csrf = False