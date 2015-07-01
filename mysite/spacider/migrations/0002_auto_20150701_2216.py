# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydata',
            name='over_3w_area',
            field=models.FloatField(verbose_name='3\u4e07\u7c73\u4ee5\u4e0a\u5c55\u89c8\u9762\u79ef\u548c'),
        ),
    ]
