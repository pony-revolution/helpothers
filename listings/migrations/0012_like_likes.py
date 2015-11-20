# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20151117_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
