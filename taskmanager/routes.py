from flask import render_template
from taskmanager import app, db
# import the class based models of db tables from models file
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")
