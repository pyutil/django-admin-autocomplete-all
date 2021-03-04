=============================
django_admin_autocomplete_all
=============================

.. image:: https://badge.fury.io/py/django-admin-autocomplete-all.svg
    :target: https://badge.fury.io/py/django-admin-autocomplete-all

.. image:: https://travis-ci.org/pyutil/django-admin-autocomplete-all.svg?branch=master
    :target: https://travis-ci.org/pyutil/django-admin-autocomplete-all

.. image:: https://codecov.io/gh/pyutil/django-admin-autocomplete-all/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pyutil/django-admin-autocomplete-all

3 different things in Django Admin:

1) Use select2 (autocomplete_fields) everywhere (because implicit is better than explicit).

2) Get more context for filtering in get_search_results; allows relative easy filtering of popup options

3) Hide danger delete/edit buttons near to the ForeignKey popups


Documentation
-------------

The full documentation is at https://django-admin-autocomplete-all.readthedocs.io.

Quickstart
----------

Install django-admin-autocomplete-all::

    pip install django-admin-autocomplete-all

Add `autocomplete_all` into `INSTALLED_APPS`, then collectstatic (both not required if you don't want enhanced get_search_results filtering.)

Features
--------

(1) **Use select2 (autocomplete_fields) everywhere.**

No need to change INSTALLED_APPS to achieve this.
In your admin.py do `import autocomplete_all as admin`.

.. code-block:: python

    import autocomplete_all as admin
    class MyModelAdmin(admin.ModelAdmin):
        ....

Alternatively import ModelAdmin, StackedInline and/or TabularInline 'from autocomplete_all' instead of 'from admin'.

.. code-block:: python

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        ....

You will then need implement lot of search_fields=.. settings in related ModelAdmins.
You can try start (ie. runserver) without adding `search_fields` and Django will show you what is required.


(2) **Get more context in get_search_results.**

Standard Django `autocomplete_fields` cannot inside `get_search_results` distinguish between the ForeignKey which asks for the queryset,
especially if 2 ForeignKey's from single model target into same model (often example: ForeignKey into User model).
If you add this package ('autocomplete_all') into INSTALLED_APPS, then ?key=... will be added into url.
Inside `get_search_results` you will have access to: application, model, ForeignKey.
See example in `static/autocomplete_all/js/autocomplete_params.js`.

 Implement filtering into get_search_results of target ModelAdmin and add this to the source ModelAdmin:

.. code-block:: python

    class MyModelAdmin(ModelAdmin):   # ModelAdmin can be standard or autocomplete_all.ModelAdmin
        class Media:
            js = ('autocomplete_all/js/autocomplete_params.js',)

You can also implement dynamic filters based on current value of other form fields.
See Usage for details or read in source code: `autocomplete_all/js/autocomplete_params.js` and `autocomplete_all.py: ModelAdmin,get_search_results_ajax`.

(3) **Hide danger buttons in Admin ChangeForm.**

The edit & delete buttons near the ForeignKey have very difficult and danger logic what they will do.
If you add `autocomplete_all` in `INSTALLED_APPS` before `django.contrib.admin` (or some application which replaces admin design, like django-baton),
then the danger buttons will disapear. Place the `autocomplete_all` "lower" in list if you don't want this effect.


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
