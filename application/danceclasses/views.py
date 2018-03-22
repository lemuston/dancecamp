from application import app, db
from flask import redirect, render_template, request, url_for
from application.danceclasses.models import Danceclass

@app.route("/danceclasses", methods=["GET"])
def danceclasses_index():
    return render_template("danceclasses/list.html", danceclasses = Danceclass.query.all())


@app.route("/danceclasses/new/")
def danceclasses_form():
    return render_template("danceclasses/new.html")

@app.route("/danceclasses/", methods=["POST"])
def danceclasses_create():
    t = Danceclass(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("danceclasses_index"))