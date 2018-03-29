from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DanceclassForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)])
#duration = IntegerField("duration")
    class Meta:
        csrf = False