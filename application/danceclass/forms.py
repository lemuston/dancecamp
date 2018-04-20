from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DanceclassForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    
    class Meta:
        csrf = False