"""
Flask-RestX API registration module
======================================
"""

from flask import Blueprint

from app.extensions import api


def init_app(app, **kwargs):
    blueprint = Blueprint('api', __name__, url_prefix='/v1/app')
    api.api.init_app(blueprint)
    app.register_blueprint(blueprint)
