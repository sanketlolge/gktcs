# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0017_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_writer', models.CharField(max_length=40)),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_content', models.TextField()),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
