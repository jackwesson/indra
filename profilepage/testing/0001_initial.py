# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepicture', models.ImageField(upload_to=b'')),
                ('description', models.CharField(max_length=5000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
