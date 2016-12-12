# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0056_auto_20160318_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table=None,
        ),
    ]
