
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application import app
from application.danceclass.forms import DanceclassForm
from application.danceclass.models import Danceclass
from application import db

@app.route("/danceclass/", methods=["GET"])
def danceclass_index():
    return render_template("danceclass/list.html", danceclasses = Danceclass.query.all()) 

@app.route("/danceclass/<string:id>/")
def danceclass_show(id):
    return render_template('danceclass/show.html', danceclass = Danceclass.query.filter_by(id=id).first())

@app.route('/danceclass/dashboard/')
def danceclass_dashboard():
    return render_template('danceclass/dashboard.html')

@app.route("/danceclass/new/")
def danceclass_form():
    return render_template("danceclass/new.html", form = DanceclassForm())

@app.route("/danceclass/", methods=["POST"])
def danceclass_create():
    form = DanceclassForm(request.form)
    t = Danceclass(form.name.data, form.length.data, form.descr.data)
    t.danceclass_id = teacher.id
  
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("danceclass_index"))

@app.route("/danceclass/delete/<string:id>", methods=["POST"])
def danceclass_delete(id):
    form = DanceclassForm(request.form)
    d = Danceclass.query.filter_by(id=id).first()
  
    db.session().delete(d)
    db.session().commit()

    return redirect(url_for("danceclass_index"))