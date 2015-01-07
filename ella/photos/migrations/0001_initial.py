# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_data.fields
import ella.photos.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('max_width', models.PositiveIntegerField(verbose_name='Max width')),
                ('max_height', models.PositiveIntegerField(verbose_name='Max height')),
                ('flexible_height', models.BooleanField(default=False, help_text='Determines whether max_height is an absolute maximum, or the formattedphoto can vary from max_height to flexible_max_height.', verbose_name='Flexible height')),
                ('flexible_max_height', models.PositiveIntegerField(null=True, verbose_name='Flexible max height', blank=True)),
                ('stretch', models.BooleanField(default=False, verbose_name='Stretch')),
                ('nocrop', models.BooleanField(default=False, verbose_name='Do not crop')),
                ('resample_quality', models.IntegerField(default=85, verbose_name='Resample quality', choices=[(45, 'Low'), (65, 'Medium'), (75, 'Good'), (85, 'Better'), (95, 'High')])),
                ('master', models.ForeignKey(blank=True, to='photos.Format', help_text='When generating formatted image, use the image formatted to master format instead of the original.Useful when editors crop certain formats by hand and you wish to re-use those coordinates automatically.', null=True, verbose_name='Master')),
                ('sites', models.ManyToManyField(to='sites.Site', verbose_name='Sites')),
            ],
            options={
                'verbose_name': 'Format',
                'verbose_name_plural': 'Formats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormatedPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', max_length=300, upload_to=b'photos/%Y/%m/%d')),
                ('crop_left', models.IntegerField()),
                ('crop_top', models.IntegerField()),
                ('crop_width', models.IntegerField()),
                ('crop_height', models.IntegerField()),
                ('width', models.PositiveIntegerField(editable=False)),
                ('height', models.PositiveIntegerField(editable=False)),
                ('format', models.ForeignKey(to='photos.Format')),
            ],
            options={
                'verbose_name': 'Formated photo',
                'verbose_name_plural': 'Formated photos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('image', models.ImageField(height_field=b'height', upload_to=ella.photos.models.upload_to, width_field=b'width', max_length=255, verbose_name='Image')),
                ('width', models.PositiveIntegerField(editable=False)),
                ('height', models.PositiveIntegerField(editable=False)),
                ('important_top', models.PositiveIntegerField(null=True, blank=True)),
                ('important_left', models.PositiveIntegerField(null=True, blank=True)),
                ('important_bottom', models.PositiveIntegerField(null=True, blank=True)),
                ('important_right', models.PositiveIntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('app_data', app_data.fields.AppDataField(default=b'{}', editable=False)),
                ('authors', models.ManyToManyField(related_name='photo_set', verbose_name='Authors', to='core.Author')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Source', blank=True, to='core.Source', null=True)),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='formatedphoto',
            name='photo',
            field=models.ForeignKey(to='photos.Photo'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='formatedphoto',
            unique_together=set([('photo', 'format')]),
        ),
    ]
