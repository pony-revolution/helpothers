from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user
