# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('unit_cost', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('subtotal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tax', models.IntegerField()),
                ('payment', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='SalesProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quanitity', models.DecimalField(max_digits=10, decimal_places=3)),
                ('product_id', models.ForeignKey(to='ventasapp.Product')),
                ('sale_id', models.ForeignKey(to='ventasapp.Sale')),
            ],
        ),
    ]
