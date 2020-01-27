=============================
django_admin_autocomplete_all
=============================

.. image:: https://badge.fury.io/py/django-admin-autocomplete-all.svg
    :target: https://badge.fury.io/py/django-admin-autocomplete-all

.. image:: https://travis-ci.org/pyutil/django-admin-autocomplete-all.svg?branch=master
    :target: https://travis-ci.org/pyutil/django-admin-autocomplete-all

.. image:: https://codecov.io/gh/pyutil/django-admin-autocomplete-all/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pyutil/django-admin-autocomplete-all

Django admin: 1) Get more context for filtering in get_search_results, 2) use select2 (autocomplete_fields) everywhere (because implicit is better than explicit).

Documentation
-------------

The full documentation is at https://django-admin-autocomplete-all.readthedocs.io.

Quickstart
----------

Install django-admin-autocomplete-all::

    pip install django-admin-autocomplete-all

Add 'autocomplete_all' into INSTALLED_APPS, then collectstatic (both not required if you don't play with get_search_results filtering.)

Features
--------

(1) **Get more context in get_search_results.** Implement filtering into get_search_results of target ModelAdmin and add this to the source ModelAdmin:

.. code-block:: python

    class MyModelAdmin(ModelAdmin):
        class Media:
            js = ('autocomplete_all/js/autocomplete_params.js',)

You can also implement dynamic filters based on current value of other form fields.
See Usage for details or read in source code: autocomplete_all/js/autocomplete_params.js


(2) **Use select2 (autocomplete_fields) everywhere.**

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
