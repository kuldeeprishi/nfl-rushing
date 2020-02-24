# encoding: utf-8
"""
Models defination for NFL
--------------------------
"""

import json
import locale
from functools import total_ordering

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

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
        data = [Player(**player) for player in self.data]
        if query:
            data = [player for player in data if query in
                    getattr(player, query_field).lower()]
        return data


class Player:
    def __init__(self, **kwargs):
        self.Player = kwargs.get("Player", None)
        self.Team = kwargs.get("Team", None)
        self.Pos = kwargs.get("Pos", None)
        self.Att = kwargs.get("Att", None)
        self.Att_G = kwargs.get("Att/G", None)
        self.Yds = Yards(kwargs.get("Yds", None))
        self.Avg = kwargs.get("Avg", None)
        self.Yds_G = kwargs.get("Yds/G", None)
        self.TD = kwargs.get("TD", None)
        self.Lng = Rush(kwargs.get("Lng", None))
        self.first = kwargs.get("1st", None)
        self.first_per = kwargs.get("1st%", None)
        self.twenty_plus = kwargs.get("20+", None)
        self.fourty_plus = kwargs.get("40+", None)
        self.FUM = kwargs.get("FUM", None)

    def as_dict(self):
        return {
            "Player": self.Player,
            "Team": self.Team,
            "Pos": self.Pos,
            "Att": self.Att,
            "Att/G": self.Att_G,
            "Yds": self.Yds.val,
            "Avg": self.Avg,
            "Yds/G": self.Yds_G,
            "TD": self.TD,
            "Lng": self.Lng.val,
            "1st": self.first,
            "1st%": self.first_per,
            "20+": self.twenty_plus,
            "40+": self.fourty_plus,
            "FUM": self.FUM,
        }



@total_ordering
class Rush:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return int(str(self.val).replace('T', '')) < int(str(other.val).replace('T', ''))

    def __eq__(self, other):
        return int(str(self.val).replace('T', '')) == int(str(other.val).replace('T', ''))

    def __repr__(self):
        return self.val



@total_ordering
class Yards:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return locale.atoi(str(self.val)) < locale.atoi(str(other.val))

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return self.val
