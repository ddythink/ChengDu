# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0007_auto_20150529_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationap',
            options={'verbose_name': '\u6587\u7ae0\u4e0e\u9879\u76ee', 'verbose_name_plural': '\u6587\u7ae0\u4e0e\u9879\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='relationas',
            options={'verbose_name': '\u6587\u7ae0\u4e0e\u5c5e\u6027', 'verbose_name_plural': '\u6587\u7ae0\u4e0e\u5c5e\u6027'},
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
    ]
