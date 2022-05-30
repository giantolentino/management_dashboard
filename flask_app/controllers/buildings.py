from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.building import Building
from flask_app.models.user import User


@app.route("/buildings")
def buildings():
    if "user_id" not in session:
        return redirect("/logout")
    buildings = Building.get_all()
    return render_template("buildings.html", buildings=buildings)


@app.route("/add/building")
def add_building():
    data = {"id": session["user_id"]}
    return render_template("add_building.html")


@app.route("/register/building", methods=["POST"])
def submit_building():
    if not Building.validate_building(request.form):
        return redirect(request.referrer)
    Building.save(request.form)
    return redirect("/buildings")


@app.route("/destroy/building/<int:id>")
def delete_building(id):
    data = {"id": id}
    Building.destroy_building(data)
    return redirect("/buildings")


@app.route("/building/<int:id>")
def show_building(id):
    data = {"id": id}
    building = Building.get_building_by_id(data)
    return render_template("show_building.html", building=building)


@app.route("/edit/building/<int:id>")
def edit_building(id):
    data = {"id": id}
    return render_template(
        "edit_building.html", building=Building.get_building_by_id(data)
    )


@app.route("/update/building", methods=["POST"])
def update_building():
    if not Building.validate_building(request.form):
        return redirect(request.referrer)
    Building.update(request.form)
    return redirect("/buildings")
