# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0006_item_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cash', models.DecimalField(default=b'min_cash', max_digits=10, decimal_places=2)),
                ('min_cash', models.DecimalField(default=200, max_digits=10, decimal_places=2)),
                ('max_cash', models.DecimalField(default=1000, max_digits=10, decimal_places=2)),
                ('withdrawal', models.IntegerField(default=0)),
            ],
        ),
    ]
