# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def render(apps, schema_editor):
    GatheringCenter = apps.get_model("listings", "GatheringCenter")

    for center in GatheringCenter.objects.all():
        if hasattr(center, '_description_rendered'):
            del center._description_rendered
        center.save()


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20151030_2003'),
    ]

    operations = [
        migrations.RunPython(render),
    ]
