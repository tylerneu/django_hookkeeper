# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0004_auto_20150818_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='pull',
            name='classes',
            field=models.ManyToManyField(to='pulls.Klass'),
        ),
    ]
