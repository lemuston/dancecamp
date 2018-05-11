from flask import Flask, render_template, redirect, request, url_for
from application import app
from application.location.models import Location
from application import db
from application.forms import LocationForm

@app.route("/location/new")
def location_form():
    return render_template("location/new.html", locationform = LocationForm())
    

@app.route("/location/", methods=["POST"])
def location_create():
    locationform = LocationForm(request.form)
    a = Location(locationform.name.data, locationform.address.data, locationform.city.data)
  
    db.session().add(a)
    db.session().commit()

    return redirect(url_for("dashboard"))

@app.route("/location/<string:id>/")
def location_show(id):
    return render_template('location/show.html', location = Location.query.filter_by(id=id).first())

@app.route("/location/delete/<string:id>", methods=["POST"])
def location_delete(id):
    l = Location.query.filter_by(id=id).first()
  
    db.session().delete(l)
    db.session().commit()

    return redirect(url_for("dashboard"))