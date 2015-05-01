# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alyan', '0004_bicycle_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='is_stolen',
            field=models.BooleanField(default=True),
        ),
    ]
