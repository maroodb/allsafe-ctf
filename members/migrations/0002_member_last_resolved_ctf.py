# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_resolved_ctf',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]