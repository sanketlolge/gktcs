# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_hire_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire',
            name='vaccancies',
        ),
    ]
