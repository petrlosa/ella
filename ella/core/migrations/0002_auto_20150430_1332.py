# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
        ('core', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishable',
            name='photo',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Photo', blank=True, to='photos.Photo', null=True),
        ),
        migrations.AddField(
            model_name='publishable',
            name='source',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Source', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=ella.core.cache.fields.CategoryForeignKey(verbose_name='Category', to='core.Category'),
        ),
        migrations.AddField(
            model_name='listing',
            name='publishable',
            field=ella.core.cache.fields.CachedForeignKey(verbose_name='Publishable', to='core.Publishable'),
        ),
        migrations.AddField(
            model_name='dependency',
            name='dependent_ct',
            field=ella.core.cache.fields.ContentTypeForeignKey(related_name='depends_on_set', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='dependency',
            name='target_ct',
            field=ella.core.cache.fields.ContentTypeForeignKey(related_name='dependency_for_set', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='category',
            name='site',
            field=ella.core.cache.fields.SiteForeignKey(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='category',
            name='tree_parent',
            field=ella.core.cache.fields.CategoryForeignKey(verbose_name='Parent category', blank=True, to='core.Category', null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Photo', blank=True, to='photos.Photo', null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=ella.core.cache.fields.CachedForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('site', 'tree_path')]),
        ),
    ]
