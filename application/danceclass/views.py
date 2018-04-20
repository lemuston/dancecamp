
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application import app
from application.danceclass.forms import DanceclassForm
from application.danceclass.models import Danceclass
from application import db

@app.route("/danceclass/", methods=["GET"])
def danceclass_index():
    return render_template("danceclass/list.html", danceclasses = Danceclass.query.all()) 

@app.route("/danceclass/new/")
@login_required
def danceclass_form():
    return render_template("danceclass/new.html", form = DanceclassForm())

@app.route("/danceclass/<danceclass_id>", methods=["POST"])
def danceclass_set_done(danceclass_id):

    t = Danceclass.query.get(danceclass_id)
    #t.done = True
    db.session().commit()
  
    return redirect(url_for("danceclass_index"))

@app.route("/danceclass/", methods=["POST"])
def danceclass_create():
    form = DanceclassForm(request.form)

    t = Danceclass(form.name.data)
  

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("danceclass_index"))

@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    danceclass = Danceclass.query.filter_by(name=oldtitle).first()
    danceclass.name = newtitle
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("name")
    danceclass = Danceclass.query.filter_by(name=title).first()
    db.session.delete(danceclass)
    db.session.commit()
    return redirect("/")