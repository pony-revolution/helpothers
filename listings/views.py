from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from guardian.shortcuts import assign_perm
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin

from helpothers.views_mixins import HelpOthersMetaDataMixin
from listings.models import GatheringCenter, Resource


class GatheringCenterView(HelpOthersMetaDataMixin, DetailView):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/detail.html'


class GatheringCenterFormMixin(object):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/form.html'
    fields = (
        'location_name', 'address', 'city', 'description', 'geoposition',
        'most_needed', 'hours', 'contact',
    )


class GatheringCenterCreateView(HelpOthersMetaDataMixin, LoginRequiredMixin, GatheringCenterFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(GatheringCenterCreateView, self).form_valid(form)
        assign_perm('listings.change_gatheringcenter', self.object.author, self.object)
        assign_perm('listings.delete_gatheringcenter', self.object.author, self.object)
        return response

    def get_success_url(self):
        return reverse('resource-review')


class GatheringCenterUpdateView(HelpOthersMetaDataMixin, PermissionRequiredMixin, GatheringCenterFormMixin, UpdateView):
    permission_required = 'listings.change_gatheringcenter'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ResourceDetailView(HelpOthersMetaDataMixin, DetailView):
    model = Resource
    template_name = 'listings/resources/detail.html'


class ResourceFormMixin(object):
    model = Resource
    template_name = 'listings/resources/form.html'
    fields = ['name', 'description', 'url']


class ResourceCreateView(HelpOthersMetaDataMixin, LoginRequiredMixin, ResourceFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(ResourceCreateView, self).form_valid(form)
        assign_perm('listings.change_resource', self.object.author, self.object)
        assign_perm('listings.delete_resource', self.object.author, self.object)
        return response

    def get_success_url(self):
        return reverse('resource-review')


class ResourceUpdateView(HelpOthersMetaDataMixin, PermissionRequiredMixin, ResourceFormMixin, UpdateView):
    permission_required = 'listings.change_resource'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ReviewView(HelpOthersMetaDataMixin, TemplateView):
    """
    Page to notify the user that the resource will be reviewed.
    """
    template_name = 'listings/resources/review.html'
