# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0009_auto_20151207_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sale_id',
            field=models.IntegerField(default=1),
        ),
    ]
