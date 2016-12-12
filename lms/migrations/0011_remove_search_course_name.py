# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0010_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='course_name',
        ),
    ]
