# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import re
import app_data.fields
import ella.core.cache.fields
from ella.utils.timezone import utc_localize
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug', validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(help_text='Description which can be used in link titles, syndication etc.', verbose_name='Description', blank=True)),
                ('content', models.TextField(default=b'', help_text='Optional content to use when rendering this category.', verbose_name='Content', blank=True)),
                ('template', models.CharField(default=b'category.html', help_text='Template to use to render detail page of this category.', max_length=100, verbose_name='Template', choices=[(b'category.html', ''), (b'static_page.html', '')])),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', validators=[django.core.validators.RegexValidator(re.compile(b'^(?:[0-9]+[^0-9-]|[a-z])[a-z0-9-]*$'), 'Please enter a valid slug composed of lowecase letter, numbers and hyphens. First character must be a letter.', b'invalid')])),
                ('tree_path', models.CharField(verbose_name='Path from root category', max_length=255, editable=False)),
                ('app_data', app_data.fields.AppDataField(default=b'{}', help_text='If you need to define custom data for category objects, you can use this field to do so.', verbose_name='Custom meta data', editable=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_id', models.IntegerField()),
                ('dependent_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Dependency',
                'verbose_name_plural': 'Dependencies',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_from', models.DateTimeField(verbose_name='Start of listing', db_index=True)),
                ('publish_to', models.DateTimeField(null=True, verbose_name='End of listing', blank=True)),
                ('commercial', models.BooleanField(default=False, help_text='Check this if the listing is of a commercial content.', verbose_name='Commercial')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='Publishable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('publish_from', models.DateTimeField(default=utc_localize(datetime.datetime(3000, 1, 1)), verbose_name='Publish from', db_index=True)),
                ('publish_to', models.DateTimeField(null=True, verbose_name='End of visibility', blank=True)),
                ('static', models.BooleanField(default=False, verbose_name='static')),
                ('last_updated', models.DateTimeField(verbose_name='Last updated', blank=True)),
                ('app_data', app_data.fields.AppDataField(default=b'{}', editable=False)),
                ('announced', models.BooleanField(default=False, help_text=b'Publish signal sent', editable=False)),
                ('authors', models.ManyToManyField(to='core.Author', verbose_name='Authors')),
                ('category', ella.core.cache.fields.CategoryForeignKey(verbose_name='Category', to='core.Category')),
                ('content_type', ella.core.cache.fields.ContentTypeForeignKey(editable=False, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Publishable object',
                'verbose_name_plural': 'Publishable objects',
            },
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('related_id', models.IntegerField(verbose_name='Object ID')),
                ('publishable', models.ForeignKey(verbose_name='Publishable', to='core.Publishable')),
                ('related_ct', ella.core.cache.fields.ContentTypeForeignKey(verbose_name='Content type', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Related',
                'verbose_name_plural': 'Related',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
    ]
