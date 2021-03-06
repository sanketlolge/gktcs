# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20150509_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Start', models.CharField(max_length=200)),
                ('Duration', models.CharField(max_length=30)),
                ('Days', models.CharField(max_length=20)),
                ('Time', models.TimeField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
