
from flask import redirect, render_template, request, url_for
from application import app
from application.danceclass.models import Danceclass
from application.teacher.models import Teacher
from application.location.models import Location
from application import db
from application.forms import DanceclassForm

@app.route("/danceclass/", methods=["GET"])
def danceclass_index():
    return render_template("danceclass/list.html", danceclasses = Danceclass.query.all(), teachers = Teacher.query.all())

@app.route("/danceclass/new/")
def danceclass_form():
    return render_template("danceclass/new.html", form = DanceclassForm(), danceclasses = Danceclass.query.all(), teachers = Teacher.query.all(), locations = Location.query.all())

@app.route("/danceclass/", methods=["POST"])
def danceclass_create():
    form = DanceclassForm(request.form)
    t = Danceclass(form.name.data, form.length.data, form.descr.data, form.teacher_id.data, form.location_id.data)
  
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("dashboard"))


@app.route("/danceclass/<string:id>/")
def danceclass_show(id):
    return render_template('danceclass/show.html', danceclass = Danceclass.query.filter_by(id=id).first())

@app.route("/danceclass/delete/<string:id>", methods=["POST"])
def danceclass_delete(id):
    d = Danceclass.query.filter_by(id=id).first()
  
    db.session().delete(d)
    db.session().commit()

    return redirect(url_for("dashboard"))