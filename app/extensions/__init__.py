# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position,wrong-import-order
"""
Extensions setup
================
Extensions provide access to common resources of the application.
Any new extension initialization and instantiations can be done here
"""


from .logging import Logging

logging = Logging()


from . import api


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in [logging]:
        extension.init_app(app)
