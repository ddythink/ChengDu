# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0013_auto_20150601_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotrack',
            name='spend_time',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
