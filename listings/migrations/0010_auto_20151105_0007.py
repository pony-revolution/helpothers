# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_gatheringcenter_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatheringcenter',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='region',
            field=models.ForeignKey(to='listings.Region', null=True),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='city',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
