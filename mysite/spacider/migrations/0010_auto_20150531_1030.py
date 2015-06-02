# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0009_infotrack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infotrack',
            old_name='data',
            new_name='run_date',
        ),
    ]
