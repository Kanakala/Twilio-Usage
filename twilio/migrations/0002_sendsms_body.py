# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendsms',
            name='body',
            field=models.CharField(default=datetime.datetime(2016, 12, 21, 14, 3, 44, 761604, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
