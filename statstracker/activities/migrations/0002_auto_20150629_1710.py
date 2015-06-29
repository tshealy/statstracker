# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='day',
        ),
        migrations.AddField(
            model_name='stats',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
