# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_signupforemail_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupforemail',
            name='day',
            field=models.CharField(default=datetime.date(2017, 6, 1), max_length=128),
            preserve_default=False,
        ),
    ]
