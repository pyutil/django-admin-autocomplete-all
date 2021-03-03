"""
In Django admin:
    - Use select2 (autocomplete_fields) everywhere. HowTo? in admin.py use: `import autocomplete_all as admin`
    - Add ?key=.. into Referer url (makes possible distinguish which ForeignKey calls an autocomplete) HowTo? add `autocomplete_all` into `INSTALLED_APPS`
    - Remove danger Edit/Delete buttons near to ForeignKey. HowTo? add `autocomplete_all` into `INSTALLED_APPS` before(!) `django.contrib.admin`
"""

from ._version import __version__


__version_info__ = VERSION = tuple(map(lambda x: int(x), __version__.split('.')))


# make this accessible at basic level as if it would be module (and not a package)
from django.contrib.admin import (AdminSite, AllValuesFieldListFilter, BooleanFieldListFilter, ChoicesFieldListFilter, DateFieldListFilter,
            EmptyFieldListFilter, FieldListFilter, HORIZONTAL, ListFilter, RelatedFieldListFilter, RelatedOnlyFieldListFilter, SimpleListFilter,
            VERTICAL, actions, apps, autodiscover, autodiscover_modules, checks, decorators, exceptions, filters, helpers,
            options, register, site, sites, templatetags, utils, views, widgets)
            # skipped: default_app_config, models (because with them it is impossible to add `autocomplete_all` into INSTALLED_APPS)
            # skipped ModelAdmin, StackedInline, TabularInline
from .autocomplete_all import ModelAdmin, StackedInline, TabularInline
