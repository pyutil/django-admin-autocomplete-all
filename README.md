# django-admin-autocomplete-all
Django admin: Use select2 (autocomplete_fields) everywhere. Implicit is better than explicit. Because it is brief and easy.
In addition gives improved context in get_search_results so you can apply filters based on current <select> and form values.

## Install

Install the last stable release

    django-admin-autocomplete-all

Add into INSTALLED_APPS:

    'autocomplete_all',

## Usage (more context for server-side filters)

Read in our Documentation (readthedocs) or in autocomplete_all/js/autocomplete_params.js.

## Usage (add all foreign keys to autocomplete_fields)

In your admin.py import ModelAdmin, StackedInline and/or TabularInline 'from autocomplete_all' instead of 'from admin'.

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        # ....

In such ModelAdmin class no other settings are required, but you can:

    autocomplete_except = [<field1>, ..]    # disable adding autocomplete_fields for listed fields 
    autocomplete_all = False                # disable automatic adding of autocomplete_fields at all

At the first start you will probably receive a lot of django errors/warnings.
They mean that you don't have registered the related ModelAdmin classes or that such class lacks search_fields=..
To solve these messages you can register the required ModelAdmin classes (make sure they have search_fields=..). See ModelAdmin.autocomplete_fields in Django docs for details.
Alternatively you can disable the functionality in particular case using autocomplete_exclude=[..]. This is useful if you have models not fully used yet (ie. empty) and you want prevent them to be accessible in admin interface.


Example:
In the application models you have ForeignKey(s) related into User model (outside of this application).
To avoid error messages while starting your Django project add:

    from django.contrib.auth.models import User
    from django.contrib.auth.admin import UserAdmin  # must define search_fields=.. (which is true in this case)
    admin.site.register(User, UserAdmin)
