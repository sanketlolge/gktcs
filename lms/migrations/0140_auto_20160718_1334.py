# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0139_auto_20160718_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='mycourse_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_img_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
