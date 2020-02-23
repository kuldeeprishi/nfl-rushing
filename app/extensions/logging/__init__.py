# encoding: utf-8
"""
Logging adapter
---------------
"""
import logging
import logging.config


class Logging(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Common Flask interface to initialize the logging according to the
        application configuration.
        """
        # We don't need the default Flask's loggers when using our invoke tasks
        # since we set up loggers globally.
        for handler in list(app.logger.handlers):
            app.logger.removeHandler(handler)
        log_config = app.config["LOGGING"]

        logging.config.dictConfig(log_config)

        app.logger.propagate = True

        if app.debug:
            app.logger.setLevel(logging.DEBUG)
