from flask_app import app
from flask import render_template, session, redirect, flash, request
from flask_app.models.user import User
from flask_app.models.author import Author


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    print(data)
    user_authors = Author.get_user_authors(data)
    return render_template("dashboard.html", user_authors=user_authors)


@app.route("/create", methods=["POST"])
def save():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect("/")

    if Author.validate_author(request.form):

        data = {
            "author_fname": request.form["author_fname"],
            "author_lname": request.form["author_lname"],
            "user_id": session["user_id"]
        }

        Author.save(data)
        flash("Author Group Created")
        return redirect("/dashboard")
    return redirect("/dashboard")
