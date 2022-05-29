from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.like import Like
from flask_app.models.user import User


@app.route("/add/like", methods=["POST"])
def add_like():
    Like.save(request.form)
    return redirect(request.referrer)
