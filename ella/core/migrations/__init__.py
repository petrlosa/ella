"""
Django migrations for ella core app
This package does not contain South migrations.  South migrations can be found
in the ``south_migrations`` package.
"""

SOUTH_ERROR_MESSAGE = """\n
For South support, customize the SOUTH_MIGRATION_MODULES setting like so:
    SOUTH_MIGRATION_MODULES = {
        'ella.core': 'ella.core.south_migrations',
    }
"""

try:
    from django.db import migrations
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)
