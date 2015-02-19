# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(serialize=False, primary_key=True)),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('class_room', models.CharField(max_length=30)),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('notes', models.CharField(max_length=30)),
                ('date_added', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InscriptionDetail',
            fields=[
                ('inscription_detail_id', models.IntegerField(serialize=False, primary_key=True)),
                ('notes', models.CharField(max_length=30)),
                ('date_added', models.DateField()),
                ('class_id', models.ForeignKey(to='lms.Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.IntegerField()),
                ('notes', models.CharField(max_length=30)),
                ('date_added', models.DateField()),
                ('active', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('notes', models.CharField(max_length=30)),
                ('date_added', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.IntegerField()),
                ('notes', models.CharField(max_length=30)),
                ('date_added', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inscriptiondetail',
            name='student_id',
            field=models.ForeignKey(to='lms.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='inscribed_students',
            field=models.ManyToManyField(to='lms.Student', through='lms.InscriptionDetail'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='subject_id',
            field=models.ForeignKey(to='lms.Subject'),
            preserve_default=True,
        ),
    ]
