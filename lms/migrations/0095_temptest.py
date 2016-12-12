# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0094_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='temptest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.BigIntegerField(blank=True)),
                ('linkedin_id', models.CharField(max_length=60, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'placement', blank=True)),
                ('city', models.CharField(max_length=15, blank=True)),
                ('des', models.TextField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
