# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0084_auto_20160323_1237'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='lms_userprofile',
        ),
    ]
