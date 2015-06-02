# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150430_1332'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('target_id', models.PositiveIntegerField(null=True, verbose_name='Target id', blank=True)),
                ('text', models.TextField(verbose_name='Definition', blank=True)),
                ('box_type', models.CharField(max_length=200, verbose_name='Box type', blank=True)),
                ('active_from', models.DateTimeField(null=True, verbose_name='Position active from', blank=True)),
                ('active_till', models.DateTimeField(null=True, verbose_name='Position active till', blank=True)),
                ('disabled', models.BooleanField(default=False, verbose_name='Disabled')),
                ('category', ella.core.cache.fields.CategoryForeignKey(verbose_name='Category', to='core.Category')),
                ('target_ct', ella.core.cache.fields.ContentTypeForeignKey(verbose_name='Target content type', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
    ]
