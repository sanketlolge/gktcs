# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0023_auto_20150721_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='register',
            name='enter_password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='re_enter_password',
            field=models.CharField(max_length=50),
        ),
    ]
