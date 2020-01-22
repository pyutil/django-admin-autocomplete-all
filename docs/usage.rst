=====
Usage
=====

In your admin.py import ModelAdmin, StackedInline and/or TabularInline from autocomplete_all instead of from admin.admin

.. code-block:: python

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        ....

In such class no other settings are required, but you can:

.. code-block:: python

    autocomplete_exclude = [<field1>, ..]    # disable adding autocomplete_fields for listed fields
    autocomplete_all = False                 # disable automatic adding of autocomplete_fields at autocomplete_all

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
