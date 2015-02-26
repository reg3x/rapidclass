# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_auto_20150225_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('evaluation_id', models.IntegerField(serialize=False, primary_key=True)),
                ('class_id', models.ForeignKey(to='lms.Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.IntegerField(serialize=False, primary_key=True)),
                ('doc_file', models.FileField(upload_to=b'documents/')),
                ('evaluation_id', models.ForeignKey(to='lms.Evaluation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
