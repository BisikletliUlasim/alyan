# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alyan', '0003_bicyclephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='city',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
