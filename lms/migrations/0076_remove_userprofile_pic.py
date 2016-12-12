# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0075_auto_20160323_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pic',
        ),
    ]
