from django.contrib import admin

from .models import Region, City, GatheringCenter, Resource

admin.site.register(Region)
admin.site.register(City)


class PublishMixin(object):
    actions = ('publish', 'unpublish')

    def publish(self, request, queryset):
        queryset.update(published=True)

    def unpublish(self, request, queryset):
        queryset.update(published=False)


class GatheringCenterAdmin(PublishMixin, admin.ModelAdmin):
    list_filter = ('published', 'city')
    list_editable = ('published', )
    list_display = ('location_name', 'published', 'author', 'city')
    raw_id_fields = ('author', )

admin.site.register(GatheringCenter, GatheringCenterAdmin)


class ResourceAdmin(PublishMixin, admin.ModelAdmin):
    list_filter = ('published', )
    list_editable = ('published', )
    list_display = ('name', 'published', 'author', 'url')
    raw_id_fields = ('author', )

admin.site.register(Resource, ResourceAdmin)


