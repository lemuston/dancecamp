from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from application.teacher import models

class RegisterForm(FlaskForm):
    account_id = StringField("account_id")
    danceclass_id = StringField("danceclass_id")
    
    class Meta:
        csrf = False

    def __init__(self, account_id, danceclass_id):
        self.account_id = account_id
        self.danceclass_id = danceclass_id