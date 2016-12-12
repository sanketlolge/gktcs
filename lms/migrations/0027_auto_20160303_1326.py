# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0026_auto_20160224_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_img_url',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_url',
            field=models.TextField(blank=True),
        ),
    ]
