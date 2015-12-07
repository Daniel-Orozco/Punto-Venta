# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0005_auto_20151207_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
    ]
