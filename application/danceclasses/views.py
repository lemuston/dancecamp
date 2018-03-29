from application import app, db
from flask import redirect, render_template, request, url_for
from flask import login_required
from application.danceclasses.models import Danceclass
from application.danceclasses.forms import DanceclassForm


@app.route("/danceclasses", methods=["GET"])
def danceclasses_index():
    return render_template("danceclasses/list.html", danceclasses = Danceclass.query.all())


@app.route("/danceclasses/new/")
@login_required
def danceclasses_form():
    return render_template("danceclasses/new.html", form = DanceclassForm())

@app.route("/danceclasses/<danceclass_id>", methods=["POST"])
@login_required
def danceclasses_set_done(task_id):

    t = Danceclass.query.get(task_id)
    #t.done = True
    db.session().commit()
  
    return redirect(url_for("danceclasses_index"))

@app.route("/danceclasses/", methods=["POST"])
def dancecamp_create():
    form = DanceclassForm(request.form)

    t = Danceclass(form.name.data)
    t.duration = form.done.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("danceclasses_index"))