# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0004_auto_20151206_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesproducts',
            old_name='quanitity',
            new_name='quantity',
        ),
    ]
