# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0014_auto_20160424_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='numid',
        ),
        migrations.AddField(
            model_name='events',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
