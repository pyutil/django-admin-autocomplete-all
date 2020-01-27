=============================
django_admin_autocomplete_all
=============================

.. image:: https://badge.fury.io/py/django-admin-autocomplete-all.svg
    :target: https://badge.fury.io/py/django-admin-autocomplete-all

.. image:: https://travis-ci.org/pyutil/django-admin-autocomplete-all.svg?branch=master
    :target: https://travis-ci.org/pyutil/django-admin-autocomplete-all

.. image:: https://codecov.io/gh/pyutil/django-admin-autocomplete-all/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pyutil/django-admin-autocomplete-all

Django admin: Use select2 (autocomplete_fields) everywhere. Implicit is better than explicit. Because it is brief and easy.

Documentation
-------------

The full documentation is at https://django-admin-autocomplete-all.readthedocs.io.

Quickstart
----------

Install django-admin-autocomplete-all::

    pip install django-admin-autocomplete-all

Add 'autocomplete_all' into INSTALLED_APPS.

Features
--------

1. You can add 'class Media: js=..' to get more context in get_search_results. You can also implement better server-side filtering in ajax calls include dynamic filters based on current value of other form fields.
Read more in Usage or in source: autocomplete_all/js/autocomplete_params.js


2. Django admin: Use select2 (autocomplete_fields) everywhere.

In your admin.py import ModelAdmin, StackedInline and/or TabularInline 'from autocomplete_all' instead of 'from admin'.

.. code-block:: python

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        ....


Running Tests
-------------

Does the code actually work? /N/A while we haven't the 1st test yet./

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  cookiecutter_
*  `cookiecutter-djangopackage`_

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
