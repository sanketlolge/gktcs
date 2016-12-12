# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0114_auto_20160330_0521'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table="'gipldb.lms_userprofile",
        ),
    ]
