from flask import Blueprint
from flask_restx import Api


api = Api(
    version="v1",
    title="Sports Service Api",
    default="nfl",
    contact="kuldeepkrishi@gmail.com",
    description="Sports API",
)


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    pass
