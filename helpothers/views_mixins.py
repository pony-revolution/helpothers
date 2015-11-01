from django.http import HttpRequest
from django.utils.translation import ugettext as _

from meta.views import MetadataMixin


# TODO this should really be in the django-meta itself, but it is faster to add a Mixin here, than send PR to django-meta
class HelpOthersMetaDataMixin(MetadataMixin):
    description = _('A collection of up to date and relevant resources on how to help the refugees')
    twitter_card = 'summary'
    twitter_site = '@z_anderle'  # TODO have a relevant Twitter account for this
    image = 'http://helpothers.eu/static/img/header.jpg'  # TODO should not be hardcoded
