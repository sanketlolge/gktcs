# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0053_auto_20160318_1137'),
    ]

    operations = [
        migrations.DeleteModel(
            name='placement_info',
        ),
    ]
