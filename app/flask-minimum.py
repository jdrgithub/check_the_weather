"""
A microservice that consumes data from external AP, transforms the data, and provides via new API endpoint.

This is the core flask template to build on.
"""

from flask import Flask
from routes import main

# Create instance of Flask class
# The __name__ variable used for setting up paths.
app = Flask(__name__)
app.register_blueprint(main)


# Define a route for root URL -> tells Flask what URL triggers `home` function.
@app.route('/')
def home():
    # `home` executed when upon access to root URL ('/')
    # Returns response message displayed in the browser
    return "TEMP TEXT"


# Server starts only if script is executed directly, not as module.
if __name__ == '__main__':
    # app.run() starts the Flask development server on http://127.0.0.1:5000
    # enables debug mode -> error messages and auto-reloads server on code change.
    app.run(debug=True)
