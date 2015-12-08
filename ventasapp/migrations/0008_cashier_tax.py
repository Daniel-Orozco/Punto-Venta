# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0007_cashier'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashier',
            name='tax',
            field=models.DecimalField(default=16, max_digits=3, decimal_places=0),
        ),
    ]
