# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-08 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_cms', '0005_auto_20170517_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('R', 'Public'), ('P', 'Pending')], default='D', max_length=150, verbose_name='Status'),
        ),
    ]
