# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0062_remove_userprofile_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': False},
        ),
    ]
