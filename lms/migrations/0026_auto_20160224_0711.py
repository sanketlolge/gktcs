# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0025_add_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_instructor',
            name='mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='Contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='hire',
            name='mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='register',
            name='contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='contactno',
            field=models.BigIntegerField(),
        ),
    ]
