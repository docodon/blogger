# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20150707_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pic',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
