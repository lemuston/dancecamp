from flask import Flask, render_template, redirect, request, url_for
from application import app
from application.danceclass.models import Danceclass
from flask_login import login_required
from application.location.models import Location
from application.teacher.models import Teacher




@app.route("/")
def index():
    return render_template("index.html", danceclasses = Danceclass.query.all(), teachers = Teacher.query.all(), locations = Location.query.all())

@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html", danceclasses = Danceclass.query.all(), teachers = Teacher.query.all(), locations = Location.query.all())

