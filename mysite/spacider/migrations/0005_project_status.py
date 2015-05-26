# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0004_auto_20150526_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, '\u5df2\u521b\u5efa'), (1, '\u6b63\u5728\u8fd0\u884c'), (2, '\u4e2d\u65ad'), (3, '\u5df2\u7ecf\u5b8c\u6210')]),
        ),
    ]
