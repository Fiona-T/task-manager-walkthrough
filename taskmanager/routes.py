from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# import the class based models of db tables from models file
from taskmanager.models import Category, Task


@app.route("/")
def home():
    # query the Tasks model, sort by id, cast to list for use in template
    tasks = list(Task.query.order_by(Task.id).all())
    # pass tasks list to template, using variable name tasks
    return render_template("tasks.html", tasks=tasks)


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


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    # get the category from the database using category_id variable
    category = Category.query.get_or_404(category_id)
    # delete the category using variable above if found
    db.session.delete(category)
    # commit the session changes
    db.session.commit()
    return redirect(url_for("categories"))


# add task page
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # Task requires category to be assigned Retrieve categories as before
    # below will generate a dropdown list for user to choose from on form
    categories = list(Category.query.order_by(Category.category_name).all())
    # if the request method is POST, then new variable task=new instance
    # of Task model, with required fields, data from form
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            # chosen from dropdown created from categories list above
            category_id=request.form.get("category_id")
        )
        # add + commit the new task to database session
        db.session.add(task)
        db.session.commit()
        # redirect to the home page after form submitted
        return redirect(url_for("home"))
    # GET method:
    # categories above is passed into the render template, using variable name
    # categories - the add_task template is expecting this variable name
    return render_template("add_task.html", categories=categories)


# edit task page, passing task_id from tasks page
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    # get the task from the database using task_id variable
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # update each column header with data from the form
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        # commit the session
        db.session.commit()
    # GET method:
    # categories + task above are passed into the render template using
    # variable name, variable name is used in the edit task template
    return render_template("edit_task.html", task=task, categories=categories)
