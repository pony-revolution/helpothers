# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20151030_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='_description_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatheringcenter',
            name='description_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')]),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='description',
            field=markupfield.fields.MarkupField(default=b'', help_text='Any additional information about this specific gathering center', rendered_field=True, blank=True),
        ),
    ]
