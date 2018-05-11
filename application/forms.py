from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, TextAreaField, SubmitField
from application import db

class DanceclassForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    length = IntegerField("length")
    descr = TextAreaField("descr")
    teacher_id = IntegerField("teacher_id")
    location_id = IntegerField("location_id")

class LocationForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    address = StringField("address")
    city = StringField("city")

class TeacherForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    descr = TextAreaField("descr")

class RegisterForm(FlaskForm):
    danceclass_id = SubmitField("danceclass_id")
    account_id = SubmitField("account_id")