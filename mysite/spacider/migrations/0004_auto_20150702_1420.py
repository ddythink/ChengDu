# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0003_auto_20150702_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='everyyear',
            old_name='show',
            new_name='show_num',
        ),
    ]
