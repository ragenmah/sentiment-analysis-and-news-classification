# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
