# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0003_auto_20151206_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='tax',
            field=models.IntegerField(default=10),
        ),
    ]
