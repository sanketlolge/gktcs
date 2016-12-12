# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0030_custom_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='linkedin_id',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
