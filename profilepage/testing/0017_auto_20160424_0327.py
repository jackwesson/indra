# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0016_events_numid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='owner',
        ),
        migrations.DeleteModel(
            name='events',
        ),
    ]