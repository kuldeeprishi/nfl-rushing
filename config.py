import os
import socket
import logging
from pathlib import Path

from flask_log_request_id import RequestIDLogFilter


class Config(object):
    # Logging settings
    LOGGING_DIR = os.getenv("LOGGING_DIR", "/tmp/")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ENV = os.getenv("ENV", "local")

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "request_id": {"()": RequestIDLogFilter},
        },
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(request_id)s %(name)s %(funcName)s:%(lineno)d %(message)s"
            }
        },
        "handlers": {
            "file": {
                "level": LOG_LEVEL,
                "class": "logging.handlers.WatchedFileHandler",
                "filename": f"{LOGGING_DIR}/app.log",
                "formatter": "standard",
                "filters": ["request_id"],
            },
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "filters": ["request_id"],
            }
        },
        "loggers": {
            "()": {
                "handlers": ["file"],
                "level": "ERROR",
                "propagate": False
            }
        },
        "root": {
            "handlers": ["file", "console"],
            "level": "INFO"
        },
    }

    SECRET_KEY = os.getenv("SECRET_KEY", "36bf368sll2349skk3f1165565e7c71")

    ENABLED_MODULES = ['api', 'nfl']
    DEBUG = False
    TESTING = False



class LocalConfig(Config):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class QAConfig(Config):
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    local=LocalConfig,
    dev=DevelopmentConfig,
    qa=QAConfig,
    test=TestConfig,
    prod=ProductionConfig,
)
