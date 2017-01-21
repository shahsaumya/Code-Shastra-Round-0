# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('task_name', models.CharField(max_length=10)),
                ('task_description', models.CharField(max_length=50)),
                ('task_picture', models.ImageField(upload_to='task_pics/', null=True, blank=True)),
                ('task_hint', models.CharField(max_length=10)),
                ('task_time', models.DurationField()),
                ('task_score', models.PositiveIntegerField()),
                ('task_nextid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('team_name', models.CharField(max_length=20)),
                ('team_id', models.CharField(max_length=10)),
                ('team_member_1', models.CharField(max_length=20)),
                ('team_member_2', models.CharField(max_length=20)),
                ('team_member_3', models.CharField(null=True, blank=True, max_length=20)),
                ('team_member_4', models.CharField(null=True, blank=True, max_length=20)),
                ('team_photo', models.ImageField(upload_to='team_pics/', null=True, blank=True)),
                ('team_score', models.PositiveIntegerField()),
                ('tasks_completed', models.PositiveIntegerField()),
                ('team_rank', models.PositiveIntegerField()),
            ],
        ),
    ]
