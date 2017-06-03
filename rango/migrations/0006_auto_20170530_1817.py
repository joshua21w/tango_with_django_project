# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='subheading',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
