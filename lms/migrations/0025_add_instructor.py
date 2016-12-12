# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0024_auto_20150721_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('course_name', models.CharField(max_length=100)),
                ('linkedin_profile', models.CharField(max_length=100)),
                ('about_course', models.TextField(max_length=150)),
                ('about_yourself', models.TextField(max_length=150)),
            ],
        ),
    ]
