# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faf', '0005_auto_20171231_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motoricsfactors',
            name='somatics',
        ),
    ]
