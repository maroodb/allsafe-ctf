# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_description', models.CharField(max_length=500)),
                ('date_start', models.DateField(default=datetime.date.today, verbose_name='Start date')),
                ('date_end', models.DateField(blank=True, verbose_name='Finish date')),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectCategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='responsables',
            field=models.ManyToManyField(to='members.Member'),
        ),
    ]
