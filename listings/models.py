from django.db import models
from django.utils.translation import ugettext as _

from geoposition.fields import GeopositionField
from model_utils.models import TimeStampedModel


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
    description = models.TextField(
        blank=True,
        default='',
        help_text=_('Any additional information about this specific gathering center')
        )
    published = models.BooleanField(blank=True, default=False)
    # TODO add information about when this center is active
    # TODO add infomartion about what is needed the most

    def __unicode__(self):
        return '%s - %s' % (self.city, self.location_name or self.address)


class Resource(TimeStampedModel):
    """
    Model for storing various helpful resources - links, other websites, etc.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    url = models.URLField(max_length=500, blank=True, default='')  # TODO do we need to worry about len(url) > 500 ?
    sticky = models.BooleanField(blank=True, default=False)
    published = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.name
