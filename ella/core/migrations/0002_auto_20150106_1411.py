# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Photo', blank=True, to='photos.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publishable',
            name='photo',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Photo', blank=True, to='photos.Photo', null=True),
            preserve_default=True,
        ),
    ]
