# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171210_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='klub', to='users.Club', verbose_name='Klub'),
        ),
        migrations.AlterField(
            model_name='club',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Adres'),
        ),
    ]
