# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170714_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='Site',
            new_name='site',
        ),
    ]
