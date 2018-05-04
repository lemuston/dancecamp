from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class DanceclassForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    length = IntegerField("length")
    descr = StringField("descr")
    
    class Meta:
        csrf = False