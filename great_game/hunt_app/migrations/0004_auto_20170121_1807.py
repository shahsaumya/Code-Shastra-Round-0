# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-21 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt_app', '0003_team_team_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='tasks_completed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
