from flask_wtf import FlaskForm
from wtforms import StringField
from application.danceclasses.views import DanceclassForm

class DanceclassForm(FlaskForm):
    name = StringField("name")
 
    class Meta:
        csrf = False