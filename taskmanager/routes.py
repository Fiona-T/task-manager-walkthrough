from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# import the class based models of db tables from models file
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# include the methods here as we submit a form on this page with POST
# @app.route("/add_category", methods=["GET", "POST"])
# def add_category():
#     # if the request method is POST, then new variable category=new instance
#     # of Category model
#     if request.method == "POST":
#         category = Category(category_name=request.form.get("category_name"))
#         # add + commit the new category to SQLAlchemy database variable of db (imported)
#         # uses sessionmaker instance
#         db.session.add(category)
#         db.session.commit()
#         # redirect the page to the categories page after form submitted
#         return redirect(url_for("categories"))
#     return render_template("add_category.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")