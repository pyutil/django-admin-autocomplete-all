=====
Usage
=====

Django admin.py files. Use ModelAdmin, StackedInline, TabularInline from autocomplete_all instead from admin.

.. code-block:: python

    import autocomplete_all
    class MyModelAdmin(autocomplete_all.ModelAdmin):
        # ....
