# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0054_delete_placement_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='career',
        ),
    ]
