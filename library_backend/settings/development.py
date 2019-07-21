from .base import *

DEBUG = get_env_variable('DEBUG_MODE')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': get_env_variable('DATABASE_HOST'),
        'PORT': get_env_variable('DATABASE_PORT'),  # Set to empty string for default.
       }
}

# toggle sentry
# if config is None, sentry will never be triggered
# if DEBUG:
#     RAVEN_CONFIG = dict()
#
RAVEN_CONFIG = dict()


# enable/disable qcount
if True:
    MIDDLEWARE += [
        'querycount.middleware.QueryCountMiddleware',
    ]

    QUERYCOUNT = {
        'THRESHOLDS': {
            'MEDIUM': 50,
            'HIGH': 200,
            'MIN_TIME_TO_LOG': 0,
            'MIN_QUERY_COUNT_TO_LOG': 0
        },
        'IGNORE_REQUEST_PATTERNS': [],
        'IGNORE_SQL_PATTERNS': [],
        'DISPLAY_DUPLICATES': 20,
    }


# enable/disable django debug toolbar
if True:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    # django debug toolbar allowed internal ips
    INTERNAL_IPS = ['127.0.0.1']
