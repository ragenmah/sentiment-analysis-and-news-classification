# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20170730_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='NegativeClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NeutralClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PositiveClassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('pubDate', models.CharField(max_length=20)),
            ],
        ),
    ]
