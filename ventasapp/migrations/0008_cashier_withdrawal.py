# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0007_cashier'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashier',
            name='withdrawal',
            field=models.IntegerField(default=0),
        ),
    ]
