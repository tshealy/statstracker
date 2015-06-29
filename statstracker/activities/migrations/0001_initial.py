# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('stat', models.IntegerField()),
                ('day', models.DateTimeField(default=django.utils.timezone.now)),
                ('activities', models.ForeignKey(to='activities.Activities')),
            ],
        ),
    ]
