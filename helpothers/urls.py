# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from helpothers.views import (HomeView, ProfileView, GatheringCenterView,
                              ResourceCreateView, ResourceDetailView, ReviewView)

admin.autodiscover()


urlpatterns = i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^center/(?P<pk>\d+)$', GatheringCenterView.as_view(), name='gathering_center'),

    url(r'^resource/(?P<pk>\d+)$', ResourceDetailView.as_view(), name='resource'),
    url(r'^resource/add$', ResourceCreateView.as_view(), name='resource-add'),
    url(r'^resource/review$', ReviewView.as_view(), name='resource-review'),

    url(r'accounts/profile', ProfileView.as_view(), name='account-profile'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),

)
