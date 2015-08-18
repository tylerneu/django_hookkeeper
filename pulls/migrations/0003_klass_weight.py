# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0002_auto_20150817_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='klass',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
