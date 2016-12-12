# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0028_auto_20160303_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_img_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Name',
            field=models.CharField(max_length=200),
        ),
    ]
