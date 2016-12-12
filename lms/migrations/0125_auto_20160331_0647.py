# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0124_userprofile'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofile',
        ),
    ]
