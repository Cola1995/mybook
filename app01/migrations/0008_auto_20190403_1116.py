# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-03 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20190329_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99.9, max_digits=5),
        ),
    ]
