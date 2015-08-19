# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Pull',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('classes', models.ManyToManyField(related_name='classes', to='pulls.Klass')),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='klass',
            field=models.ForeignKey(to='pulls.Klass'),
        ),
        migrations.AddField(
            model_name='entry',
            name='pull',
            field=models.ForeignKey(to='pulls.Pull'),
        ),
        migrations.AddField(
            model_name='entry',
            name='tractor',
            field=models.ForeignKey(to='pulls.Tractor'),
        ),
    ]
