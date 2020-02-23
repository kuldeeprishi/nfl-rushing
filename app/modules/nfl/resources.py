# encoding: utf-8
"""
RESTx API NFL resources
--------------------------
"""

import logging
import locale
import traceback
import json
import csv
from math import ceil
from tempfile import TemporaryFile

from flask_csv import send_csv

from flask import request, current_app, Response
from flask_restx import Namespace, Resource
from .parser import nfl_filters
from .models import NFL
from .utils import get_paginated_data

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

api = Namespace('nfl', description="National Football League")


@api.route('')
class NFLResource(Resource):

    @api.expect(nfl_filters)
    def get(self):
        """
        Get NFL Data.
        For now the data is being loaded from rushing.json that is places in
        project root dir.
        """
        response = {}

        args = nfl_filters.parse_args(request)

        page = args.get("page")
        per_page = args.get("per_page")
        query = args.get("query")
        query_by = args.get("query_by")
        sort_by = args.get("sort_by")
        sort = args.get("sort")
        output = args.get("output")

        nfl_data = NFL().query(query, query_by)

        if sort_by:
            reverse = sort == 'desc'
            nfl_data = sorted(nfl_data,
            key=lambda k: locale.atoi(str(k[sort_by])), reverse=reverse)

        count = len(nfl_data)
        total_pages = ceil(count / per_page)

        if page != 1 and page > total_pages:
            response['status'] = 'error'
            response['message'] = f'Invalid Page Number: {page}'
            return response, 400

        data = get_paginated_data(nfl_data, page, per_page)

        response['status'] = 'success'
        response['message'] = f'found {count} events'
        response['page'] = page
        response['per_page'] = per_page
        response['total_pages'] = total_pages
        response['data'] = data

        if output == 'csv':
            try:
                headers = data[0].keys()
            except IndexError:
                headers = []
            return send_csv(data, 'data.csv', headers)

        return response, 200
