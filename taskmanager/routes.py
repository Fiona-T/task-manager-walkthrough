from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# import the class based models of db tables from models file
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # query the Category model, sort by name, cast to list for use in template
    # as .all() returns a cursor object
    categories = list(Category.query.order_by(Category.category_name).all())
    # pass categories list to template, using variable name categories
    return render_template("categories.html", categories=categories)


# include the methods here as we submit a form on this page with POST
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # if the request method is POST, then new variable category=new instance
    # of Category model
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        # add + commit the new category to SQLAlchemy database variable of
        # db (imported). Uses sessionmaker instance
        db.session.add(category)
        db.session.commit()
        # redirect the page to the categories page after form submitted
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# edit category page, passing category_id from categories page
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # get the category from the database using category_id variable
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        # set category variable cat name to name attribute from form
        category.category_name = request.form.get("category_name")
        # commit the session
        db.session.commit()
        # redirect to the categories page after the edit form is submitted
        return redirect(url_for("categories"))
    # GET method:
    # category above is passed into the render template, using variable name
    # category - the template is expecting this variable name
    return render_template("edit_category.html", category=category)
