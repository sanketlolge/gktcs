# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0089_auto_20160326_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='des',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table=None,
        ),
    ]
