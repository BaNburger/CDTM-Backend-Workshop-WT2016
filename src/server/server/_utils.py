<<<<<<< HEAD
from flask import abort, jsonify, make_response
=======
from flask import abort, jsonify, make_response, request

from functools import wraps
import re

from server import *
from server.database import db_list_exists
>>>>>>> a83a7489063e43be574973a2d7a89a365895e035

def json_abort(code, text):
    json = {
        'result': False,
        'error': {
            'status': code,
            'text': text
        }
    }
    abort(make_response(jsonify(json), code))
<<<<<<< HEAD
=======

 # --------------------
 # ---  DECORATORS  ---
 # --------------------

def has_json(f):
    ''' Checks whether a request provides json'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
             data = request.get_json()
        except:
            json_abort(400, 'No JSON provided')

        if data == None:
            json_abort(400, 'Invalid Content-Type')

        return f(*args, **kwargs)
    return decorated_function


def list_exists(f):
    ''' Checks whether a list exists with id 'list_id' exists'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        list_id = kwargs.get('list_id')
        if not db_list_exists(list_id):
            json_abort(404, 'List not found')
        return f(*args, **kwargs)
    return decorated_function
>>>>>>> a83a7489063e43be574973a2d7a89a365895e035
