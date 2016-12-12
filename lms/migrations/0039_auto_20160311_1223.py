# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0038_auto_20160311_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='user_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
