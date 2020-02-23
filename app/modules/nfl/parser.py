from flask_restx import reqparse

nfl_filters = reqparse.RequestParser()

nfl_filters.add_argument(
    'query', type=str, required=False,
    help='query data using given keyword. By default query on player name')

nfl_filters.add_argument(
    'query_by', type=str, required=False,
    choices=['Player', 'Team'], default='Player',
    help='used along with query to query on given field')

nfl_filters.add_argument(
    'sort_by', type=str, required=False,
    choices=['Yds', 'Lng', 'TD'],
    help='sort result by selected field')

nfl_filters.add_argument(
    'sort', type=str, required=False,
    choices=['asc', 'desc'], default='desc',
    help='sort result asscending or decending')


nfl_filters.add_argument(
    'output', type=str, required=False,
    choices=['csv'],
    help='output the response in given format')
