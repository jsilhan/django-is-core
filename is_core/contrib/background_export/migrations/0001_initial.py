# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-18 18:10
from __future__ import unicode_literals

import chamber.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import is_core.contrib.background_export.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('security', '0012_auto_20190815_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportedFile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('slug', models.SlugField(max_length=32, primary_key=True, serialize=False, verbose_name='slug')),
                ('file', chamber.models.fields.FileField(blank=True, null=True, upload_to=is_core.contrib.background_export.models.generate_filename, verbose_name='file')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_exported_files', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('downloaded_by', models.ManyToManyField(blank=True, related_name='downloaded_exported_files', to=settings.AUTH_USER_MODEL, verbose_name='downloaded by')),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='security.CeleryTaskLog', verbose_name='state')),
            ],
            options={
                'verbose_name': 'exported file',
                'verbose_name_plural': 'exported files',
                'ordering': ('-created_at',),
            },
        ),
    ]
