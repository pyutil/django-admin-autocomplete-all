=====
Usage
=====

This package has 3 independent functions:

1. Add autocomplete_fields for all foreign keys. (no need to change `INSTALLED_APPS`, but in admin.py do `import autocomplete_all as admin`)

2. Add ?key=... into url to have more information inside get_search_results. (requires adding of `autocomplete_all` into `INSTALLED_APPS`)

3. Hide danger delete/edit buttons near the ForeignKey popup (`INSTALLED_APPS`: place `autocomplete_all` before `django.contrib.admin`)


.. contents:: Contents
--------------

1. Add autocomplete_fields for all foreign keys.
---------------------------------------------

To achieve this, in your `admin.py` do: `import autocomplete_all as admin`.

.. code-block:: python

    import autocomplete_all as admin
    class MyModelAdmin(admin.ModelAdmin):
        ....

Alternatively import ModelAdmin, StackedInline and/or TabularInline from `autocomplete_all` instead of from `admin`

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


2. Get more context in get_search_results for better filtering.
---------------------------------------------------------------

To achieve this, add `autocomplete_all` into INSTALLED_APPS. The Referer url will then contain `?key=...`

If you want **2 dependent popups** (example: Country/City):

.. code-block:: python

    # from django.contrib import admin
    import autocomplete_all as admin
    
    from .models import City, Country, Friend
    
    
    @admin.register(Country)
    class CountryAdmin(admin.ModelAdmin):
        search_fields = ('name',)
    
    
    @admin.register(City)                                                                # Target admin (searches for popup options)
    class CityAdmin(admin.ModelAdmin):
        search_fields = ('name',)
        
        def get_search_results_ajax(self, queryset, referer, key, urlparams):
            if referer.startswith('friends/friend/'):   # <app>/<model>/  # model of the Source (which has popup) Admin (not of the Inline)

                # example for the plain popup
                if key == 'id_city':                    # <field ~ foreignkey>
                    queryset = queryset.filter(country=urlparams['country'][0])

                # example for the popup inside the Inline (which lists more locations)
                if key.startswith(before := 'id_location_set-') and key.endswith(after := '-city'):
                    idx = key[len(before):-len(after)]
                    queryset = queryset.filter(country=urlparams[f'location_set-{idx}-country'][0])

            return queryset

    
    @admin.register(Friend)
    class FriendAdmin(admin.ModelAdmin):   # if you don't need ModelAdmin you can use HiddenAdmin instead
        search_fields = ('nick',)

        # no more needed here; autocomplete_all.js is automatically added and gives all forms values in the urlparams variable

        # but alternatively you can limit the form values transferred by the ajax request:
        # class Media:
        #     js = ('autocomplete_all/js/autocomplete_all.js', 'friends/js/friend.js')   # Source admin

        # `friends.js` you need to create inside the `friends` application. Here is example:
        #
        #    function expand_ajax_params($, key) {
        #        return '&country=' + $('#id_country').val();
        #    }

Previous will give required data for your `.get_search_results_ajax()` method (of the relational targeted ModelAdmin).
That way you can control queryset filtering based on: 1) application, 2) model (where in change_form the popup is), 3) the ForeignKey of the popup.


Especially previous is **workaround for stupid behaviour of autocomplete_fields** in Django (2,3).
Probably you cannot modify the native Django ajax url (../autocomplete/) and you can only access the Referer url during get_search_results.

Lets say, **you have inside single model 2 <select>s with same target model of ForeignKey** (example: User, in two different roles).
In such case you cannot identify on the server-side (in get_search_results) which one <select> is active.
This package will extend the Referer url to give more info to the server-side.

Basically ?key=<fieldname> will be added to identify the <select>.

For dynamic filters (dependent on current value of other field in your admin form) you should add second (yours) ModelAdmin Media js file and rewrite inside it the function expand_ajax_params.
Read more above. You will find more in sources: `autocomplete_all/js/autocomplete_all.js`, `autocomplete_all.py: ModelAdmin.get_search_results_ajax`


3. Hide danger buttons in Admin ChangeForm.
-------------------------------------------

The edit & delete buttons near the ForeignKey have very difficult and danger logic what they will do.
If you add `autocomplete_all` in `INSTALLED_APPS` before `django.contrib.admin` (or some application which replaces admin design, like `django-baton`),
then the danger buttons will disapear. Place the `autocomplete_all` "lower" in `INSTALLED_APPS` if you don't want this effect.
