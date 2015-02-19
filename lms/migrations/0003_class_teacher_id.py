# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20150219_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='teacher_id',
            field=models.ForeignKey(default=1, to='lms.Teacher'),
            preserve_default=False,
        ),
    ]
