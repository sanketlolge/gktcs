# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0033_auto_20160311_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='user_image',
            field=models.ImageField(null=True, upload_to=b'/home/gktcs/public_html/GLMS/static/placement', blank=True),
        ),
    ]
