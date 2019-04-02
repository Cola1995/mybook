# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-26 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('book', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]
