# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0096_delete_enroll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temptest',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='temptest',
            name='user',
        ),
    ]
