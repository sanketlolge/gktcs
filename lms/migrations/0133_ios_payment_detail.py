# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0132_delete_ios'),
    ]

    operations = [
        migrations.CreateModel(
            name='IOS',
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
            name='Payment_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instamojo_name', models.CharField(max_length=50)),
                ('payment_id', models.CharField(unique=True, max_length=40)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default=b'payable', max_length=20)),
                ('success', models.BooleanField(default=False)),
                ('instamojo_email_id', models.EmailField(max_length=254)),
                ('instamojo_contact_no', models.BigIntegerField()),
                ('course_selected', models.CharField(max_length=50)),
                ('course_fees', models.CharField(max_length=50)),
                ('query_url', models.URLField(default=b'https://www.instamojo.com/api/1.1/payments/')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
