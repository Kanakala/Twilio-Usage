# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_auto_20161221_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('body', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='sendsms',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sendsms',
            name='body',
            field=models.CharField(max_length=4),
        ),
    ]
