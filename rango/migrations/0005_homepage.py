# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Heading', models.CharField(unique=True, max_length=128)),
                ('subheading', models.IntegerField(max_length=128)),
                ('text', models.IntegerField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
