# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20151031_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatheringcenter',
            name='contact',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
