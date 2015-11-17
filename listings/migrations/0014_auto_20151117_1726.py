# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20151117_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatheringcenter',
            name='description_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')]),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='most_needed_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')]),
        ),
    ]
