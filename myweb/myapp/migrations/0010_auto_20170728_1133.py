# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170725_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='published_date',
        ),
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
