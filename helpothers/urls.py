# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from helpothers.views import (HomeView, ProfileView, GatheringCenterView,
                              ResourceCreateView, ResourceDetailView, ReviewView,
                              LoginView, GatheringCenterCreateView)


urlpatterns = i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),

    # Centers
    url(r'^center/(?P<pk>\d+)$', GatheringCenterView.as_view(), name='gathering-center'),
    url(r'^center/add$', GatheringCenterCreateView.as_view(), name='gathering-center-add'),

    # Resources
    url(r'^resource/(?P<pk>\d+)$', ResourceDetailView.as_view(), name='resource'),
    url(r'^resource/add$', ResourceCreateView.as_view(), name='resource-add'),
    url(r'^resource/review$', ReviewView.as_view(), name='resource-review'),

    url(r'accounts/profile', ProfileView.as_view(), name='account-profile'),

    # Authentication
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

)
