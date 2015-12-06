# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0002_auto_20151119_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_type',
            field=models.CharField(default=b'unit', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
