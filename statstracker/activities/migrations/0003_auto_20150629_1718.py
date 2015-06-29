# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20150629_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='created',
        ),
        migrations.AddField(
            model_name='activities',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 21, 18, 24, 133013, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
