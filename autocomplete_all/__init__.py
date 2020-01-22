"""
Django admin: Use select2 (autocomplete_fields) everywhere.
"""

from ._version import __version__


__version_info__ = VERSION = tuple(map(lambda x: int(x), __version__.split('.')))


# make this accessible at basic level as if it would be module (and not a package)
from .autocomplete_all import ModelAdmin, StackedInline, TabularInline
