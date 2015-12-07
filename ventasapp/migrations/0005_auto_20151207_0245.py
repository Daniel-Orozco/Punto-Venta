# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0004_auto_20151207_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.DecimalField(max_digits=10, decimal_places=3)),
                ('product_id', models.ForeignKey(to='ventasapp.Product')),
                ('sale_id', models.ForeignKey(to='ventasapp.Sale')),
            ],
        ),
        migrations.RemoveField(
            model_name='salesproducts',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='salesproducts',
            name='sale_id',
        ),
        migrations.DeleteModel(
            name='SalesProducts',
        ),
    ]
