# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_batches'),
    ]

    operations = [
        migrations.CreateModel(
            name='hire',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=200)),
                ('vaccancies', models.IntegerField()),
                ('job_description', models.CharField(max_length=20)),
                ('Desired_profile', models.CharField(max_length=20)),
                ('Experience', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=20)),
                ('person_name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('companyurl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('contactno', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('skills', models.CharField(max_length=20)),
                ('aboutCourse', models.CharField(max_length=100)),
                ('about_ourself', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=50)),
            ],
        ),
    ]
