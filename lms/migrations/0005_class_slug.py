# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_auto_20150219_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='slug',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
