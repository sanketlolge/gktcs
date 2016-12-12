# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0137_auto_20160718_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('course_description', models.TextField()),
                ('course_url', models.URLField(null=True, blank=True)),
                ('course_img_url', models.ImageField(null=True, upload_to=b'courses/logos', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='My_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courses_enrolled', models.ManyToManyField(to='lms.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
