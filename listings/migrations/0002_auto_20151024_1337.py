# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatheringcenter',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
