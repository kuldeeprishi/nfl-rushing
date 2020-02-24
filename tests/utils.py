"""
Testing utils
-------------
"""

from contextlib import contextmanager
from datetime import datetime, timedelta
import json

from flask import Response
from flask.testing import FlaskClient
from werkzeug.utils import cached_property


class JSONResponse(Response):
    # pylint: disable=too-many-ancestors
    """
    A Response class with extra useful helpers, i.e. ``.json`` property.
    """

    @cached_property
    def json(self):
        return json.loads(self.get_data(as_text=True))
