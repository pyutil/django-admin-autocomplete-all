.. :changelog:

History
-------

0.4.0 (2021-03-04)
expand_ajax_location_search func renamed to expand_ajax_params (incompatible change: please rename the function if you have it in your javascript)
wrapper for queryset filtering moved from example (ie. from commented code) to real code; new method .get_search_results_ajax() in ModelAdmin
new documentation in usage.rst
++++++++++++++++++

0.3.0 (2021-03-03)
++++++++++++++++++

* if used in INSTALLED_APPS before django.contrib.admin (or admin rewriting app), danger ForeignKey buttons (edit,delete) will disapear
* import admin methods (example: .register): in many cases you can just `import autocomplete_all as admin` and no more changes in admin.py are needed

0.2.6 (2020-05-06)
++++++++++++++++++

* Fix: added class Media to fix some scenario(s) where widget is missing

0.2.4 (2020-01-27)
++++++++++++++++++

* gives additional context in get_search_results()
* Fix: missing .js (in 0.2.0-0.2.3)

0.1.6 (2020-01-24)
++++++++++++++++++

* Fix in docs: proper attribute name is: autocomplete_except

0.1.4 (2020-01-22)
++++++++++++++++++

* First acceptable version.
