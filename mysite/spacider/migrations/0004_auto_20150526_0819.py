# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0003_auto_20150526_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source_site',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='source_site_url',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='source_url',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='spider_from',
            field=models.IntegerField(default=0, choices=[(1, b'wuchong'), (2, b'junpeng'), (0, b'no set')]),
        ),
    ]
