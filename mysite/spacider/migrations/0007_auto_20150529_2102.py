# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0006_article_crawler_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': ' \u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '\u9879\u76ee', 'verbose_name_plural': '\u9879\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='relationas',
            options={'verbose_name': '\u6587\u7ae0\u5c5e\u6027', 'verbose_name_plural': '\u6587\u7ae0\u5c5e\u6027'},
        ),
        migrations.AlterModelOptions(
            name='ruler',
            options={'verbose_name': '\u89c4\u5219', 'verbose_name_plural': '  \u89c4\u5219'},
        ),
        migrations.AlterModelOptions(
            name='siteproperty',
            options={'verbose_name': '\u5c5e\u6027', 'verbose_name_plural': '\u5c5e\u6027'},
        ),
        migrations.AddField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 13, 2, 16, 719809, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ruler',
            name='attr',
            field=models.ForeignKey(default=1, to='spacider.Siteproperty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='other',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='thetype',
            field=models.IntegerField(choices=[(0, '\u4f1a\u5c55\u8bc4\u4f30'), (1, '\u5a92\u4f53\u8bc4\u4f30')]),
        ),
        migrations.AlterField(
            model_name='relationap',
            name='article',
            field=models.ForeignKey(to='spacider.Article'),
        ),
        migrations.AlterField(
            model_name='relationap',
            name='project',
            field=models.ForeignKey(to='spacider.Project'),
        ),
        migrations.AlterField(
            model_name='relationas',
            name='article',
            field=models.ForeignKey(to='spacider.Article'),
        ),
        migrations.AlterField(
            model_name='relationas',
            name='site_property',
            field=models.ForeignKey(to='spacider.Siteproperty'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='enable',
            field=models.IntegerField(default=1, choices=[(0, '\u672a\u542f\u7528'), (1, '\u542f\u7528')]),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='flag',
            field=models.SmallIntegerField(default=1, choices=[(1, '\u81ea\u52a8\u83b7\u5f97'), (2, '\u5f85\u7ea0\u6b63'), (3, '\u5df2\u786e\u5b9a')]),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='nature',
            field=models.SmallIntegerField(default=3, choices=[(1, '\u5b98\u7f51'), (2, '\u4f1a\u5c55\u7c7b\u7f51'), (3, '\u666e\u901a\u7f51'), (4, '\u5927\u578b\u65b0\u95fb\u7f51')]),
        ),
    ]
