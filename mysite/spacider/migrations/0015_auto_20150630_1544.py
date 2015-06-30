# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0014_infotrack_spend_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotrack',
            name='project',
            field=models.ForeignKey(related_name='infotrack_ids', to='spacider.Project'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u89c4\u5219\u540d'),
        ),
    ]
