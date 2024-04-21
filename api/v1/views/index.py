#!/usr/bin/python3
""" Checks if there is a connection """
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Gives status """
    return jsonify({'status': 'OK'})
