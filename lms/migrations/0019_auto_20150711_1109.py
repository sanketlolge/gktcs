# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0018_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
