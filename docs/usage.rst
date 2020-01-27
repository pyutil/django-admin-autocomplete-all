=====
Usage
=====

This package has 2 independent functions:

1. Get more context in get_search_results for better filtering include dynamic filters based on current values of other form fields.

2. Add autocomplete_fields for all foreign keys.

--------------

Get more context in get_search_results for better filtering.
------------------------------------------------------------

This is workaround for stupid behaviour of autocomplete_fields in Django (2,3).
Probably you cannot modify the native Django ajax url (../autocomplete/) and you can only access the Referer url during get_search_results.

Lets say, you have 2 <select>s with same ForeignKey (example: User, in two different roles).
In such case you cannot identify on the server-side (in get_search_results) which one <select> is active.
This package will extend the Referer url to give more info to the server-side.
Basically ?key=<fieldname> will be added to identify the <select>
but you can add more (see later) and implement dynamic filters (dependent on current form values) too.

EXAMPLE:

source ModelAdmin:

.. code-block:: python

    class Media:
        js = ('autocomplete_all/js/autocomplete_params.js',)

target ModelAdmin:

.. code-block:: python

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.is_ajax and '/autocomplete/' in request.path:
            url = urllib.parse.urlparse(request.headers['Referer'])
            referer = url.path
            qs = urllib.parse.parse_qs(url.query)
            if '/npo/finding/' in referer:            # /<app>/<model>/
                if qs.get('key') == ['id_process']:   # <field ~ foreignkey> (parse_qs results are lists)
                    queryset = queryset.filter(...)
        return queryset, use_distinct

If you need dynamic filter based on current value of other field in your admin form then you can add second (yours) ModelAdmin Media js file and rewrite in it the function expand_ajax_location_search.
You will find complete example in sources: at bottom of autocomplete_all/js/autocomplete_params.js

--------------

Add autocomplete_fields for all foreign keys.
---------------------------------------------

In your admin.py import ModelAdmin, StackedInline and/or TabularInline from autocomplete_all instead of from admin.admin

.. code-block:: python

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        ....

In such class no other settings are required, but you can:

.. code-block:: python

    autocomplete_except = [<field1>, ..]    # disable adding autocomplete_fields for listed fields
    autocomplete_all = False                # disable automatic adding of autocomplete_fields at all

At the first start you will probably receive a lot of django errors/warnings.
They mean that you don't have registered the related ModelAdmin classes or that such class lacks search_fields=..

To solve these messages you can register the required ModelAdmin classes (make sure they have search_fields=..). See ModelAdmin.autocomplete_fields in Django docs for details.

Alternatively you can disable the functionality in particular case using autocomplete_exclude=[..]. This is useful if you have models not fully used yet (ie. empty) and you want prevent them to be accessible in admin interface.


Example:
In the application models you have ForeignKey(s) related into User model (outside of this application).
To avoid error messages while starting your Django project add:

.. code-block:: python

    from django.contrib.auth.models import User
    from django.contrib.auth.admin import UserAdmin  # must define search_fields=.. (which is true in this case)
    admin.site.register(User, UserAdmin)
