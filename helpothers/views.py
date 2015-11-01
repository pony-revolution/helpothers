from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from guardian.shortcuts import assign_perm
from guardian.mixins import PermissionRequiredMixin
from listings.models import GatheringCenter, Resource


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gathering_centers'] = GatheringCenter.objects.filter(published=True)
        context['resources'] = Resource.objects.filter(published=True)
        return context


class LoginView(TemplateView):
    template_name = 'login.html'


class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class GatheringCenterView(DetailView):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/detail.html'


class GatheringCenterFormMixin(object):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/form.html'
    fields = (
        'location_name', 'address', 'city', 'description', 'geoposition',
        'most_needed', 'hours', 'contact',
    )


class GatheringCenterCreateView(GatheringCenterFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(GatheringCenterCreateView, self).form_valid(form)
        assign_perm('listings.change_gatheringcenter', self.object.author, self.object)
        assign_perm('listings.delete_gatheringcenter', self.object.author, self.object)
        return response

    def get_success_url(self):
        return reverse('resource-review')


class GatheringCenterUpdateView(PermissionRequiredMixin, GatheringCenterFormMixin, UpdateView):
    permission_required = 'listings.change_gatheringcenter'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'listings/resources/detail.html'


class ResourceFormMixin(object):
    model = Resource
    template_name = 'listings/resources/form.html'
    fields = ['name', 'description', 'url']


class ResourceCreateView(ResourceFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(ResourceCreateView, self).form_valid(form)
        assign_perm('listings.change_resource', self.object.author, self.object)
        assign_perm('listings.delete_resource', self.object.author, self.object)
        return response

    def get_success_url(self):
        return reverse('resource-review')


class ResourceUpdateView(PermissionRequiredMixin, ResourceFormMixin, UpdateView):
    permission_required = 'listings.change_resource'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ReviewView(TemplateView):
    """
    Page to notify the user that the resource will be reviewed.
    """
    template_name = 'listings/resources/review.html'
