# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0077_auto_20160323_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.BigIntegerField()),
                ('linkedin_id', models.CharField(max_length=60, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'/', blank=True)),
                ('user', models.OneToOneField(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
