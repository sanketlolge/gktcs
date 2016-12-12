# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0069_auto_20160323_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.BigIntegerField()),
                ('linkedin_id', models.CharField(max_length=60, blank=True)),
            ],
            options={
                'db_table': 'userprofile',
                'managed': False,
            },
        ),
    ]
