# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0003_klass_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klass',
            old_name='tractor',
            new_name='tractors',
        ),
    ]
