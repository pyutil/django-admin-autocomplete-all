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


Important note
--------------
There are many ways how to include autocomplete support for ForeignKeys in Django.

Here we have a manual way, which probably is not good way to go, but we can understand how the things could work internally: https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html

The robust industrial and standard way (I think so) is the usage of django-autocomplete-light. The package can be used outside of and inside in the django Admin.
This requires lot of clones of very similar code: 1) in urls.py to attach all ajax entrypoints,
2) in views.py lot of ajax views based on autocomplete.Select2QuerySetView with get_queryset() method which handles the seeked string and optionally the from client forwarded filtering values,
3) the forms which attach the autocomplete.ModelSelect2 widgets,
4) inside the admin.py the attaching of such forms to ModelAdmin or Inlines.

It is (django-autocomplete-light) clean and easy solution. However with 20 models in db schema previous can be a difficult work for many hours where you can make lot of mistakes.
This is probably one area where django-admin-autocomplete-all can be easier and faster to implement:
Just turn it on (see Usage) and `./manage.py check` will write where you need add a ModelAdmin (or alternativelly HiddenAdmin) and define its get_search_results (or get_search_results_ajax) method.

So it is one way how to go: inside Admin django-admin-autocomplete-all and outside of Admin django-autocomplete-light.
However after some tweaking I see the idea of Django 2+ autocomplete_fields (used by django-admin-autocomplete-all) as pure implemented.
So I will personally prefer use of the great django-autocomplete-light package everywhere.
Thats why you cannot wait big improvements of this package in the future.
But I think with Py 3.9, Dj 3.1 it simple works.

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

(1) **Add autocomplete_fields for all foreign keys.**

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


(2) **Get more context in get_search_results for additional dynamic filtering.**

Standard Django `autocomplete_fields` cannot inside `get_search_results` distinguish between the ForeignKey which asks for the queryset,
especially if 2 ForeignKey's from single model target into same model (often example: ForeignKey into User model).
If you add this package ('autocomplete_all') into INSTALLED_APPS, then ?key=... will be added into url.
Inside `get_search_results` you will have access to: application, model, ForeignKey.
See example in `static/autocomplete_all/js/autocomplete_all.js`.

You need implement filtering into get_search_results of target ModelAdmin (you can use HiddenAdmin class instead).
Instead of get_search_results you can use get_search_results_ajax which run for the autocomplete/ access only.

You can also implement dynamic filters based on current value of other form fields.
See Usage for details or read in source code: `autocomplete_all/js/autocomplete_all.js` and `autocomplete_all.py: ModelAdmin,get_search_results_ajax`.

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
