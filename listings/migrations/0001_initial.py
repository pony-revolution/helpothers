# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GatheringCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('location_name', models.CharField(default=b'', help_text='If this center has any special name', max_length=100, blank=True)),
                ('address', models.CharField(max_length=255)),
                ('geoposition', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
                ('description', models.TextField(default=b'', help_text='Any additional information about this specific gathering center', blank=True)),
                ('city', models.ForeignKey(to='listings.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=b'', blank=True)),
                ('url', models.URLField(default=b'', max_length=500, blank=True)),
                ('sticky', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, to='listings.Region', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'region')]),
        ),
    ]
