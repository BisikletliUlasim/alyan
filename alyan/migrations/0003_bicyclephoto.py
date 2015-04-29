# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alyan', '0002_bicycle_registration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BicyclePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('bicycle', models.ForeignKey(to='alyan.Bicycle')),
            ],
        ),
    ]
