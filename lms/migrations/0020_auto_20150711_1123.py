# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0019_auto_20150711_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_date',
            field=models.DateField(),
        ),
    ]
