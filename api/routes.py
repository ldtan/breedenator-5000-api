"""
This file contains all routes of the application. All routes should be register
here for the application to recognize.
"""

# [START of Imports]
from flask_lazyviews import LazyViews
# [END of Imports]

def create_routes(api):
    controllers = LazyViews(api, 'api.controllers')
    controllers.add('/', 'sample.index', methods=['GET'])
