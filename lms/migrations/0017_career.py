# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0016_delete_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_name', models.CharField(max_length=20)),
                ('post_desc', models.TextField()),
            ],
        ),
    ]
