from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.comment import Comment
from flask_app.models.user import User


@app.route("/add/comment", methods=["POST"])
def add_comment():
    Comment.save(request.form)
    return redirect(request.referrer)


@app.route("/destroy/comment/<int:id>")
def delete_comment(id):
    data = {"id": id}
    Comment.destroy_comment(data)
    return redirect(request.referrer)
