# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0008_auto_20150529_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infotrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('add_num', models.IntegerField(default=0)),
                ('sum', models.IntegerField()),
                ('spider_from', models.IntegerField(default=0, choices=[(1, b'wuchong'), (2, b'junpeng'), (0, b'no set')])),
                ('project', models.ForeignKey(to='spacider.Project')),
            ],
            options={
                'verbose_name': '\u722c\u866b\u52a8\u6001',
                'verbose_name_plural': '\u722c\u866b\u52a8\u6001',
            },
        ),
    ]
