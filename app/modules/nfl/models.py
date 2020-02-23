# encoding: utf-8
"""
Models defination for NFL
--------------------------
"""

import json


class NFL:
    def __init__(self):
        self.data =  self._get_data()

    def _get_data(self):
        '''
        Get NFL data. This function can be customized to load data from
        anysource. For now this will load data from the rushing.json present in
        project root dir
        '''
        return json.load(open('./rushing.json')) or []

    def query(self, query, query_field):
        data = self.data
        if query:
            data = [player for player in data if query in
                    player.get(query_field).lower()]

        return data

