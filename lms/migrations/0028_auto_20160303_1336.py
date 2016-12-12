# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0027_auto_20160303_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Name',
            field=models.CharField(max_length=250),
        ),
    ]
