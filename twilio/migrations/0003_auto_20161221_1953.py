# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_sendsms_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendsms',
            name='delivered_at',
        ),
        migrations.RemoveField(
            model_name='sendsms',
            name='sent_at',
        ),
    ]
