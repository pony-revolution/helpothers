from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .views_mixins import HelpOthersMetaDataMixin
from listings.models import GatheringCenter, Resource


class HomeView(HelpOthersMetaDataMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gathering_centers'] = GatheringCenter.objects.filter(published=True)
        context['resources'] = Resource.objects.filter(published=True)[0:3]
        return context


class LoginView(HelpOthersMetaDataMixin, TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        ctx = super(LoginView, self).get_context_data(**kwargs)
        ctx['next'] = self.request.GET.get('next')
        return ctx


class LoginErrorView(TemplateView):
    template_name = 'errors/login.html'


class ProfileView(HelpOthersMetaDataMixin, UpdateView):
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'
    fields = ('user__first_name', 'user__last_name', 'user__email')

    def get_object(self, queryset=None):
        return self.request.user.profile
