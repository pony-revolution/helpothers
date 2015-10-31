# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20151030_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatheringcenter',
            name='_most_needed_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='hours',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='most_needed',
            field=markupfield.fields.MarkupField(default=b'', rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='most_needed_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')]),
        ),
    ]
