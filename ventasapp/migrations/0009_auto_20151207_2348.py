# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0008_cashier_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cashier',
            name='tax',
            field=models.IntegerField(default=10),
        ),
    ]
