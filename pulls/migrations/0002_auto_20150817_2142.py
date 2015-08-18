# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klass',
            name='tractor',
        ),
        migrations.AddField(
            model_name='klass',
            name='tractor',
            field=models.ManyToManyField(to='pulls.Tractor'),
        ),
    ]
