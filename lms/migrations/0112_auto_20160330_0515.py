# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0111_auto_20160330_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=b'DEFAULT VALUE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table=None,
        ),
    ]
