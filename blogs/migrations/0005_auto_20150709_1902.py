# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_author_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='pic',
            new_name='image',
        ),
    ]
