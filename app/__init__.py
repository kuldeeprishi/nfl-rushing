import os
import sys
import logging
import uuid
import time
import json

from flask import Flask, jsonify, render_template
from flask_log_request_id import RequestID, current_request_id

from config import config_by_name

environment = os.getenv('ENV', 'local')
settings = config_by_name[environment]()


def create_app(config_name=None):
    app = Flask(__name__)

    env_name = os.getenv("ENV")
    if not env_name and config_name is None:
        config_name = "local"
    elif config_name is None:
        config_name = env_name
    else:
        if env_name:
            assert env_name == config_name, (
                'ENV environment variable ("%s") and config_name argument '
                '("%s") are both set and are not the same.'
                % (env_name, config_name)
            )

    print(f"Loading {env_name} configuration")

    try:
        app.config.from_object(config_by_name[config_name])
    except ImportError:
        if config_name == "local":
            app.logger.error(  # pylint: disable=no-member
                "You have to have `local` defined in the configuration in order to use "
                "the default 'local' Flask Config. Alternatively, you may set `ENV` "
                "environment variable to one of the following options: dev, qa, test, prod"
            )
            sys.exit(1)
        raise


    RequestID(app, request_id_generator=lambda: f"NFL{uuid.uuid4().hex}")

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    return app

app = create_app()


@app.after_request
def append_request_id(response):
    response.headers.add("X-REQUEST-ID", current_request_id())
    return response
