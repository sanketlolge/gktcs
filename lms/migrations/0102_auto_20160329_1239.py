# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0101_temptest_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='temptest',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='userprofile',
        ),
    ]
