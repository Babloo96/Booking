# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20170712_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_availability',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
    ]
