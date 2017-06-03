# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20170531_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupforemail',
            name='created',
            field=models.DateTimeField(default=datetime.date(2017, 6, 1), auto_now_add=True),
            preserve_default=False,
        ),
    ]
