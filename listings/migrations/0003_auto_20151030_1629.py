# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20151024_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
