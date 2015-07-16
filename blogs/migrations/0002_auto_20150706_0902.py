# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='handle',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
