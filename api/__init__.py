"""
This file initializes your application and brings together all of the various
components.
"""

# [START of Imports]
import os
from flask import Flask
from routes import create_routes
# [END of Imports]

def create_api(name=None, **options):
    api = Flask(name or __name__, instance_relative_config=True)
    api.config.update(options)

    # Load the default configuration
    api.config.from_object('config.default')

    # Load the configuration from the instance folder
    api.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    api.config.from_object(os.getenv('APP_CONFIG_FILE', 'config.development'))

    create_routes(api)

    return api
