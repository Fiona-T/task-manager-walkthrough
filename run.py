import os
from taskmanager import app

# to get the app running - check is name class equal to main
# if it is, then run the app with the parameters below
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=os.environ.get("DEBUG")
    )
