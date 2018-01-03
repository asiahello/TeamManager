# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0004_auto_20180102_1043'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SwotAnalyzis',
            new_name='SwotAnalysis',
        ),
        migrations.AlterField(
            model_name='playerfactor',
            name='swot_category',
            field=models.CharField(choices=[('STRENGTH', 'MOCNE STRONY'), ('WEAKNESS', 'S?ABE STRONY'), ('UNKNOWN', 'NIEPRZYPISANE')], default='UNKNOWN', max_length=15, verbose_name='klasyfikacja'),
        ),
    ]
