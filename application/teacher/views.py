
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application import app
from application.teacher.models import Teacher
from application.forms import TeacherForm
from application import db


@app.route("/teacher/new/")
def teacher_form():
    return render_template("teacher/new.html", teacherform = TeacherForm())
    return redirect(url_for("dashboard"))

@app.route("/teacher/", methods=["POST"])
def teacher_create():
    teacherform = TeacherForm(request.form)
    a = Teacher(teacherform.name.data, teacherform.descr.data)
  
    db.session().add(a)
    db.session().commit()

    return redirect(url_for("dashboard"))


@app.route("/teacher/<string:id>/")
def teacher_show(id):
    return render_template('teacher/show.html', teacher = Teacher.query.filter_by(id=id).first())

@app.route("/teacher/delete/<string:id>", methods=["POST"])
def teacher_delete(id):
    d = Teacher.query.filter_by(id=id).first()
  
    db.session().delete(d)
    db.session().commit()

    return redirect(url_for("dashboard"))