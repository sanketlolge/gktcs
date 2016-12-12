# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0109_auto_20160329_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': False},
        ),
    ]
