# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_auto_20150519_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='Email',
            new_name='email',
        ),
    ]
