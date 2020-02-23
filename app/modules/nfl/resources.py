# encoding: utf-8
"""
RESTx API NFL resources
--------------------------
"""

import logging
import traceback
import json

from flask import request, current_app
from flask_restx import Namespace, Resource


api = Namespace('nfl', description="National Football League")


@api.route('')
class NFLResource(Resource):
    def get(self):
        """
        Get NFL Data.
        For now the data is being loaded from rushing.json that is places in
        project root dir.
        """
        return json.load(open('./rushing.json')), 200

