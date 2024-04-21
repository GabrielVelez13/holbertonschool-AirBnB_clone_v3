#!/usr/bin/python3
""" Flask app """

# Importing necessary modules
from models import storage  # Importing storage from models
from api.v1.views import app_views  # Importing app_views from api.v1.views
from os import environ  # Importing environ from os for environment variables
from flask import Flask  # Importing Flask class from flask module

# Creating an instance of the Flask class
app = Flask(__name__)
# Setting strict_slashes to False to allow for trailing slashes in the URL
app.url_map.strict_slashes = False
# Registering the blueprint app_views with the Flask application instance
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """ 
    This function is called when the application context is torn down.
    It closes the storage
    """
    storage.close()

if __name__ == "__main__":
    """ 
    This block is only executed when the script is run directly, not when it's imported.
    It connects to the host
    """
    # Getting the host and port from environment variables
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    # If host or port is not set in environment variables, set them to default values
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    # Running the Flask application instance
    app.run(host=host, port=port, threaded=True)
