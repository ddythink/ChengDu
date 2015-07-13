# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='nati_confe',
            field=models.IntegerField(default=0, verbose_name='\u56fd\u9645\u4f1a\u8bae\u4e2a\u6570'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u7c7b\u578b', choices=[(0, '\u4f1a\u5c55\u62a5\u544a'), (1, '\u5a92\u4f53\u62a5\u544a'), (2, '\u76f8\u540c\u5730\u533a'), (3, '\u4e0d\u540c\u5730\u533a'), (4, '\u57ce\u5e02\u5bf9\u6bd4')]),
        ),
    ]
