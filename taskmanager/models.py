from taskmanager import db


# define the class based models for the two tables, using default
# declaritive base from SQLAlchemy's Model
class Category(db.Model):
    # scheme for the Category model - column names
    # db contains column types (Integer etc.), so can use dot notation,
    # do not need to import them at top of file
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # to link this table to the Category table one to many relationship
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represent itself (class object) as a string
        # can also use __str__
        return self.category_name


class Task(db.Model):
    # scheme for the Task model - column names
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # represent itself (class object) as a string
        # can also use __str__
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )

        # could have used fstring
        # return f"
        #   #{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"
