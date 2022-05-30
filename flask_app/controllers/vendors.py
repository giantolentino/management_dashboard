from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.vendor import Vendor
from flask_app.models.comment import Comment


@app.route("/vendors")
def vendors():
    if "user_id" not in session:
        return redirect("/logout")
    vendors = Vendor.get_all()
    return render_template("vendors.html", vendors=vendors)


@app.route("/add/vendor")
def add_vendor():
    data = {"id": session["user_id"]}
    return render_template("add_vendor.html")


@app.route("/register/vendor", methods=["POST"])
def submit_vendor():
    if Vendor.validate_vendor(request.form):
        Vendor.save(request.form)
        return redirect("/vendors")
    return redirect(request.referrer)


@app.route("/destroy/vendor/<int:id>")
def delete_vendor(id):
    data = {"id": id}
    Vendor.destroy_vendor(data)
    return redirect("/vendors")


@app.route("/vendor/<int:id>")
def show_vendor(id):
    data = {"id": id}
    user_data = {"id": session["user_id"]}
    user = User.get_by_id(user_data)
    vendor = Vendor.get_vendor_by_id(data)
    comments = Comment.get_comments_by_vendors_id(data)
    return render_template(
        "show_vendor.html", user=user, vendor=vendor, comments=comments
    )


@app.route("/edit/vendor/<int:id>")
def edit_vendor(id):
    data = {"id": id}
    return render_template("edit_vendor.html", vendor=Vendor.get_vendor_by_id(data))


@app.route("/update/vendor", methods=["POST"])
def update_vendor():
    if Vendor.validate_vendor(request.form):
        Vendor.update(request.form)
        return redirect("/vendors")
    return redirect(request.referrer)
