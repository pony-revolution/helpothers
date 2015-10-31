from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from django_countries.fields import CountryField
from geoposition.fields import GeopositionField
from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = CountryField(null=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'region')
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __unicode__(self):
        return self.name


class GatheringCenter(TimeStampedModel):
    location_name = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text=_('If this center has any special name')
        )
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City)
    geoposition = GeopositionField(blank=True, null=True)
    description = MarkupField(
        blank=True,
        default='',
        default_markup_type='markdown',
        help_text=_('Any additional information about this specific gathering center')
        )
    published = models.BooleanField(blank=True, default=False)
    hours = models.TextField(blank=True)
    most_needed = MarkupField(
        blank=True,
        default='',
        default_markup_type='markdown',
    )
    author = models.ForeignKey(User, null=True)
    # TODO add infomartion about what is needed the most

    def __unicode__(self):
        return '%s - %s' % (self.city, self.location_name or self.address)


class Resource(TimeStampedModel):
    """
    Model for storing various helpful resources - links, other websites, etc.
    """
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, default='')
    url = models.URLField(_('URL'), max_length=500, blank=True, default='')  # TODO do we need to worry about len(url) > 500 ?
    sticky = models.BooleanField(blank=True, default=False)
    published = models.BooleanField(blank=True, default=False)
    country = CountryField(null=True)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.name
