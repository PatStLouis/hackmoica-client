from flask import current_app as app
from flask import render_template

@app.route("/", methods=["GET"])
def index():
    return render_template("pages/landing.jinja")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("pages/login.jinja")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("pages/dashboard.jinja")

@app.route("/secret", methods=["GET"])
def secret():
    return render_template("pages/secret.jinja")