from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Region, City, GatheringCenter, Resource


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = _("Mark selected stories as published")


admin.site.register(Region)
admin.site.register(City)


class ResourceAdmin(admin.ModelAdmin):
    actions = [make_published]
    list_filter = ['published']
    list_display = ['name', 'published']


admin.site.register(Resource, ResourceAdmin)


class GatheringCenterAdmin(admin.ModelAdmin):
    actions = [make_published]
    list_filter = ['published', 'city', 'city__region']
    list_display = ['location_name', 'published', 'city']

admin.site.register(GatheringCenter, GatheringCenterAdmin)
