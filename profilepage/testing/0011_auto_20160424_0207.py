# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0010_event_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]