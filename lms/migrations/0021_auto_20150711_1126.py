# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0020_auto_20150711_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_date',
            field=models.DateTimeField(),
        ),
    ]
