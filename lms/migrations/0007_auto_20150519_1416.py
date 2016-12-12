# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_hire_vaccancies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.IntegerField()),
                ('Batch', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='technology',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('technology', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='enroll',
            name='Technology',
            field=models.ForeignKey(to='lms.technology'),
        ),
    ]
