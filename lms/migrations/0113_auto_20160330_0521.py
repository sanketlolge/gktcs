# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0112_auto_20160330_0515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': False},
        ),
    ]
