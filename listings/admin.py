from django.contrib import admin

from .models import Region, City, GatheringCenter, Resource


admin.site.register(Region)
admin.site.register(City)
admin.site.register(GatheringCenter)
admin.site.register(Resource)

