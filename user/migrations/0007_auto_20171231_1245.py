# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_player_somatics_factors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='motorics_factors',
        ),
        migrations.RemoveField(
            model_name='player',
            name='somatics_factors',
        ),
    ]
