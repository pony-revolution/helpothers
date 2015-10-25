# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from helpothers.views import HomeView, ProfileView, LoginView

admin.autodiscover()


urlpatterns = i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'accounts/profile', ProfileView.as_view(), name='account-profile'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),

)
