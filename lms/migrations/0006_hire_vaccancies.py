# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_remove_hire_vaccancies'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='vaccancies',
            field=models.IntegerField(default=0),
        ),
    ]
