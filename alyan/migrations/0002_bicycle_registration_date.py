# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('alyan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name=b'Date registered'),
        ),
    ]
