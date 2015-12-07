# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0003_auto_20151205_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesproducts',
            old_name='quanitity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='sale',
            name='tax',
            field=models.IntegerField(default=10),
        ),
    ]
