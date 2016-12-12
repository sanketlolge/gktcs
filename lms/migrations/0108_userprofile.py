# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0107_auto_20160329_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.BigIntegerField(blank=True)),
                ('linkedin_id', models.CharField(max_length=60, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'placement', blank=True)),
                ('city', models.CharField(max_length=15, blank=True)),
                ('des', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'userprofile',
                'managed': False,
            },
        ),
    ]
