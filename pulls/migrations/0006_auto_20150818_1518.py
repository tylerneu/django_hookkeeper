# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0005_pull_classes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klass',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
    ]
