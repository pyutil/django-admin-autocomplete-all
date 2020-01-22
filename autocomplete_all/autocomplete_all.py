from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    """
    Edit form in Admin based on this class has all related fields with autocomplete/search/select2 support.
    (except of: has defined autocomplete_fields or is marked as autocomplete_all=False)

    If used as the parent class in Admin, you will probably get few messages about missing and necessary
    Admin registrations and about missing search_fields=.. in already registered classes.
    Please make the suggested (and required) changes by hand.
    """
    autocomplete_all = True

    def __init__(self, model, *args, **kwargs):
        _modify_class(self, model)
        super().__init__(model, *args, **kwargs)


class StackedInline(admin.StackedInline):
    """
    Modification of StackedInline with autocomplete for all many_to_one and many_to_many fields.
    """
    autocomplete_all = True

    def __init__(self, *args, **kwargs):
        _modify_class(self, self.model)
        super().__init__(*args, **kwargs)


class TabularInline(admin.TabularInline):
    """
    Modification of TabularInline with autocomplete for all many_to_one and many_to_many fields.
    """
    autocomplete_all = True

    def __init__(self, *args, **kwargs):
        _modify_class(self, self.model)
        super().__init__(*args, **kwargs)


def _modify_class(model_admin_or_inline, model):
    """
    Fills autocomplete_fields with specified values.

    :param model_admin_or_inline: class to be modified
    :param model: model of the class
    :return: nothing (side effect - modification of class)
    """
    if model_admin_or_inline.autocomplete_all and not model_admin_or_inline.autocomplete_fields:
        autocomplete_except = getattr(model_admin_or_inline, 'autocomplete_except', [])
        acf = []
        for fld in model._meta.get_fields():
            if (fld.many_to_one or fld.many_to_many) and (fld.name not in autocomplete_except):
                acf.append(fld.name)
        if acf:
            model_admin_or_inline.autocomplete_fields = acf
