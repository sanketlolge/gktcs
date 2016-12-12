# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_auto_20150519_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='Technology',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='technology',
        ),
    ]
