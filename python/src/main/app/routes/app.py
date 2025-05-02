from flask import Flask

# Creating a Web App
app = Flask(__name__)


# Running the app
app.run(host = '0.0.0.0', port = 5000)