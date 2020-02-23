# encoding: utf-8
"""
NFL module
============
"""

from app.extensions.api import api


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init NFL module.
    """
    from . import resources  # pylint: disable=unused-import

    api.add_namespace(resources.api)
