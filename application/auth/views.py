from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

# Kirjautumislomake ja tunnistautuminen
@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm(), action="auth_login", button="Login")

    form = LoginForm(request.form)
    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, action="auth_login", button="Login",
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))

# Uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# Käyttäjän luontilomake
@app.route("/auth/new", methods=["GET"])
def auth_new():
    return render_template("auth/loginform.html", form=LoginForm(), action="auth_create", button="Create")

# Käyttäjän tallennus
@app.route("/auth/new", methods=["POST"])
def auth_create():
    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form=form, action="auth_create", button="Create")
    user = User(form.username.data.capitalize(),
                form.username.data, form.password.data)
    if bool(user.name):
        db.session().add(user)
        db.session().commit()
        login_user(user)
    return redirect(url_for("index"))
