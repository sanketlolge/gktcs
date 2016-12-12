# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0136_auto_20160718_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b'/home/gktcs/public_html/GLMS/public/static/placement/default_pic.jpg', null=True, upload_to=b'placement', blank=True),
        ),
    ]
