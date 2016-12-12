# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0011_remove_search_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='search1',
            new_name='s',
        ),
    ]
