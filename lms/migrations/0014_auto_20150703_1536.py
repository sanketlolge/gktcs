# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_placement_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=20)),
                ('course_desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='placement_info',
            name='imgstud',
            field=models.ImageField(upload_to=b'C:/GLMS/static/placement'),
        ),
    ]
