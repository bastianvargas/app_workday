# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-12 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workday_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='workday',
            name='schedule',
        ),
        migrations.AddField(
            model_name='schedule',
            name='workday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workday_app.Workday'),
        ),
    ]