# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0010_auto_20150531_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotrack',
            name='run_date',
            field=models.DateTimeField(),
        ),
    ]
