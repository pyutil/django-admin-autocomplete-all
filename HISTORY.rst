.. :changelog:

History
-------

0.6.3 (2021-03-10)
++++++++++++++++++
INCOMPATIBLE: MediaMixin renamed to AutocompleteAllMixin (please rename if you have this class in your code)

0.6.0 (2021-03-09)
INCOMPATIBLE: autocomplete_params.js renamend to autocomplete_all.js (please rename if you have this in your code)
autocomplete_all.js is now always attached in MediaMixin [later: AutocompleteAllMixin] (for ModelAdmin and both Inlines)
ajax autocomplete call now contains all values from the form (see the urlparams variable): you can easier make filtered popups
++++++++++++++++++

0.5.0 (2021-03-05)
HiddenAdmin: allow make related admins for search_fields=.. but hide them for direct access (example: we have them better accessible as Inlines)
++++++++++++++++++

0.4.0 (2021-03-04)
INCOMPATIBLE: expand_ajax_location_search func renamed to expand_ajax_params (please rename the function if you have it in your javascript)
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
