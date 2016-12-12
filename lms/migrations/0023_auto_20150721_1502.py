# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0022_forgot_login_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='enter_Password',
            new_name='enter_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='re_enter_Password',
            new_name='re_enter_password',
        ),
    ]
