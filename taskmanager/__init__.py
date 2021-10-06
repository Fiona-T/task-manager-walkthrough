import os
# import Flask class from flask
from flask import Flask
# import SQLAlchemy class from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# to use the hidden env variables, import env file but check if exists first
# as file will not be visible when deployed to Heroku so would throw an error
if os.path.exists("env.py"):
    import env  # noqa

# create instance of imported Flask class, takes default __name__ module
app = Flask(__name__)
# config variables, set to get their respective environment variable
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# for database url config variable, need to specify which url path to use
# there are two versions of db, one local and one in Heroku
# if env variable DEVELOPMENT is set to true, use the local database path DB_URL
# otherwise (as this is not set in Heroku), use Heroku path DATABASE_URL
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# create instance of imported SQLAlchemy class, set to our instance of Flask
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
