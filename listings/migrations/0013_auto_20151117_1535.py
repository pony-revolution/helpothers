# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_like_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='likes',
            new_name='like',
        ),
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name=b'Content ID'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
