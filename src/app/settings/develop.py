import os

import dj_database_url

from app.settings.common import *

DATABASES["default"] = dj_database_url.parse(os.environ["DATABASE_URL"])

DEBUG = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django": {"handlers": ["console"], "propagate": True, "level": "INFO"},
        "gunicorn": {"handlers": ["console"], "level": "DEBUG"},
    },
}
