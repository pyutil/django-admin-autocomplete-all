import urllib

from django.conf import settings
from django.contrib import admin
from django.urls import reverse


if not settings.configured:
    settings.configure()   # required for docs: make html


# this mixin was added in 0.3 because it could fix problems with missing autocomplete widget in some scenario(s)
class MediaMixin:
    # here we use files distributed inside django 2+
    class Media:
        extra = '' if settings.DEBUG else '.min'
        css = {
            "screen": (
                'admin/css/vendor/select2/select2%s.css' % extra,
                'admin/css/autocomplete.css',
            )
        }
        js = (
            'admin/js/vendor/select2/select2.full%s.js' % extra,
            'admin/js/autocomplete.js',
        )

    """
    # this is setting for dal & dal_select2

    class Media:
        css = {
            "all": (
                'vendor/select2/dist/css/select2.css',
                'autocomplete_light/select2.css',
            )
        }
        js = (
            # 'jquery/jquery-3.4.1.min.js',            # we believe jquery is loaded
            'autocomplete_light/jquery.init.js',
            'autocomplete_light/autocomplete.init.js',
            'vendor/select2/dist/js/select2.full.js',
            'autocomplete_light/select2.js',
            'autocomplete_light/forward.js',
            'autocomplete_light/jquery.post-setup.js',
        )
    """


class ModelAdmin(admin.ModelAdmin, MediaMixin):
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

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.is_ajax and '/autocomplete/' in request.path:
            strip_begin = reverse('admin:index')
            url = urllib.parse.urlparse(request.headers['Referer'])
            referer = url.path                    # example: /admin/friends/friend/add, /admin/friends/friend/36/change
            referer = referer[len(strip_begin):]  # example: friends/friend/add, friends/friend/36/change
            urlparams = urllib.parse.parse_qs(url.query)  # example: {'key': ['id_city'], 'country': '1'}  # the 2nd one from customized function expand_ajax_params
            key = urlparams.get('key')            # example: ['id_city']
            if type(key) in (list, tuple):
                key = key[0]
            queryset = self.get_search_results_ajax(queryset, referer, key, urlparams)   # filtering of queryset if it is dependent
        return queryset, use_distinct

    def get_search_results_ajax(self, queryset, referer, key, urlparams):
        return queryset
        # customization example - in inherited ModelAdmin class:
        # if referer.startswith('friends/friend/'):   # <app>/<model>/  # model of the Source admin (which has popup),
        #                                                               # not of this one (Target) admin who owns get_search_results_ajax method
        #     if key == 'id_city':                    # <field ~ foreignkey>
        #         queryset = queryset.filter(country=urlparams['country'][0])
        # return queryset
        #
        # # in addition you need in Source admin class Media, something like:
        #     class Media:
        #         js = ('autocomplete_all/js/autocomplete_params.js', 'friends/js/friend.js')
        # # and the 2nd .js must rewrite the function which expands url parameters:
        #     function expand_ajax_params($, key) {return '&country=' + $('#id_country').val();}


class StackedInline(admin.StackedInline, MediaMixin):
    """
    Modification of StackedInline with autocomplete for all many_to_one and many_to_many fields.
    """
    autocomplete_all = True

    def __init__(self, *args, **kwargs):
        _modify_class(self, self.model)
        super().__init__(*args, **kwargs)


class TabularInline(admin.TabularInline, MediaMixin):
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
