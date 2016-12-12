# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0128_auto_20160331_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_instructor',
            name='linkedin_profile',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
