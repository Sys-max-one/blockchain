from flask import Flask
from python.src.main.app.routes.mining import setup_mining_routes

# Creating a Web App
# The first argument is the name of the application’s module or package.
# __name__ is a convenient shortcut for this that is appropriate for most cases.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)
setup_mining_routes(app)

# Running the app
#$ flask run --host=0.0.0.0
# This tells your operating system to listen on all public IPs.
app.run(host = '0.0.0.0', port = 5000)