"""
This is a sample controller file.
"""

from flask import jsonify

def index():
    return jsonify({
        'message': 'Hello World!'
    })
