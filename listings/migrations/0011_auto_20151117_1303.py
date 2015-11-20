# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('listings', '0010_auto_20151105_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to='profiles.Profile')),
            ],
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='description_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')]),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='most_needed_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, blank=True, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')]),
        ),
        migrations.AlterField(
            model_name='gatheringcenter',
            name='region',
            field=models.ForeignKey(blank=True, to='listings.Region', null=True),
        ),
    ]
