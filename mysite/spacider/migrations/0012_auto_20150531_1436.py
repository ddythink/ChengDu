# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0011_auto_20150531_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infotrack',
            old_name='sum',
            new_name='sum_total',
        ),
    ]
