from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from geoposition import Geoposition
from guardian.shortcuts import assign_perm
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin

from helpothers.views_mixins import HelpOthersMetaDataMixin
from listings.models import GatheringCenter, Resource, Like

# Added by jonathan
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

class GatheringCenterView(HelpOthersMetaDataMixin, DetailView):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/detail.html'


class GatheringCenterFormMixin(object):
    model = GatheringCenter
    template_name = 'listings/gathering_centers/form.html'
    fields = (
        'location_name', 'address', 'city', 'country', 'region',
        'description', 'geoposition', 'most_needed', 'hours', 'contact',
    )


class GatheringCenterCreateView(HelpOthersMetaDataMixin, LoginRequiredMixin, GatheringCenterFormMixin, CreateView):
    initial = {
        'geoposition': Geoposition(*settings.DEFAULT_MAP_CENTER),
        'country': 'SI'
    }

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


class LikeView(TemplateView, View):
    """ This view is invoked whenever a like button gets clicked on the resource details page """

    def get(self, request):
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        resources = Resource.objects.all()

        return render(request, 'listings/resources/add_like.html', {
            'resources': resources,
        })

    def post(self, request):
        if request.user.is_authenticated():
            # We get the resource object
            resource_object = Resource.objects.get(pk=request.POST.get('resource_id'))

            # We test whether the user already liked the resource
            if(Like.objects.filter(object_id=request.POST.get('resource_id'), user=request.user).exists()):
                return HttpResponse('exists')
            else:
                # then we create a like object and finally save it...
                like = Like(content_object=resource_object, user=request.user)
                like.like += 1
                try:
                    like.save()
                    return HttpResponse('success')
                except:
                    return HttpResponse("An Error Occured");
        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
