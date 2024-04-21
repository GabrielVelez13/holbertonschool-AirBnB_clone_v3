#!/usr/bin/python3
""" Checks if there is a connection """
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Gives status """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_of_objects():
    """ Gets the number of classes """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_of_objs = {}
    for cls in range(len(classes)):
        num_of_objs[names[cls]] = storage.count(classes[cls])

    return jsonify(num_of_objs)
