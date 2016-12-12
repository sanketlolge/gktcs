# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0129_auto_20160331_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='mycourse_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
