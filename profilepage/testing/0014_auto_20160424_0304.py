# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 03:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0013_auto_20160424_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue_name', to=settings.AUTH_USER_MODEL),
        ),
    ]