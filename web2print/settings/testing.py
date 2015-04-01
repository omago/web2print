from web2print.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'oms',                     # Or path to database file if using sqlite3.
        'NAME': 'web2print',                     # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'omago',
        'PASSWORD': 'omago.123',
        'HOST': '127.0.0.1',    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',             # Set to empty string for default.
    }
}
