# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_part',
        ),
        migrations.RemoveField(
            model_name='event',
            name='intro_part',
        ),
        migrations.RemoveField(
            model_name='event',
            name='main_part',
        ),
        migrations.AddField(
            model_name='event',
            name='exercises',
            field=models.ManyToManyField(to='trainings.Exercise'),
        ),
    ]
