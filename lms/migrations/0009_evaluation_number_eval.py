# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_evaluation_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='number_eval',
            field=models.IntegerField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
