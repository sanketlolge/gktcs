# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0130_courses_mycourse_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Android',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='AngularJS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Appium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Data_Science',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Hadoop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='iOS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Java',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='R_Programming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
        migrations.CreateModel(
            name='Ruby_on_Rails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=12, null=True, choices=[(b'Easy', b'Easy'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced')])),
                ('notes', models.FileField(null=True, upload_to=b'notes/', blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
            ],
            options={
                'permissions': (('is_subscribed', 'is subscribed'),),
            },
        ),
    ]
