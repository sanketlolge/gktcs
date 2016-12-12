# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0012_auto_20150626_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='placement_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('imgstud', models.ImageField(upload_to=b'')),
                ('imgcmp', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
