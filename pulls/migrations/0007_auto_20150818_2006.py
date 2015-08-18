# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0006_auto_20150818_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klass',
            name='tractors',
        ),
        migrations.AlterField(
            model_name='pull',
            name='classes',
            field=models.ManyToManyField(related_name='classes', to='pulls.Klass'),
        ),
    ]
