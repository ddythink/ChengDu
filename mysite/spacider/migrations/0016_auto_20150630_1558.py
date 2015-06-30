# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0015_auto_20150630_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(null=True, verbose_name='\u6587\u7ae0\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='crawler_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u722c\u53d6\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_time',
            field=models.DateTimeField(verbose_name='\u6587\u7ae0\u516c\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='source_site',
            field=models.CharField(max_length=256, null=True, verbose_name='\u6e90\u7ad9', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='spider_from',
            field=models.IntegerField(default=0, verbose_name='\u6765\u6e90', choices=[(1, b'wuchong'), (2, b'junpeng'), (0, b'no set')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='\u6587\u7ae0\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=256, verbose_name='\u6587\u7ae0URL'),
        ),
        migrations.AlterField(
            model_name='infotrack',
            name='add_num',
            field=models.IntegerField(default=0, verbose_name='\u589e\u52a0\u6570\u76ee'),
        ),
        migrations.AlterField(
            model_name='infotrack',
            name='run_date',
            field=models.DateTimeField(verbose_name='\u8fd0\u884c\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='infotrack',
            name='spend_time',
            field=models.IntegerField(null=True, verbose_name='\u82b1\u8d39\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='infotrack',
            name='spider_from',
            field=models.IntegerField(default=0, verbose_name='\u722c\u53d6\u6765\u6e90', choices=[(1, b'wuchong'), (2, b'junpeng'), (0, b'no set')]),
        ),
        migrations.AlterField(
            model_name='infotrack',
            name='sum_total',
            field=models.IntegerField(verbose_name='\u603b\u5171\u6570\u76ee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u9879\u76ee\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='\u4f1a\u5c55\u7ed3\u675f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='final_time',
            field=models.DateTimeField(null=True, verbose_name='\u9879\u76ee\u7ed3\u675f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='keywords',
            field=models.CharField(max_length=256, verbose_name='\u5173\u952e\u5b57'),
        ),
        migrations.AlterField(
            model_name='project',
            name='other',
            field=models.CharField(max_length=256, null=True, verbose_name='\u5176\u4ed6', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='pname',
            field=models.CharField(max_length=256, verbose_name='\u9879\u76ee\u540d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='\u4f1a\u5c55\u5f00\u59cb\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u9879\u76ee\u72b6\u6001', choices=[(0, '\u5df2\u521b\u5efa'), (1, '\u6b63\u5728\u8fd0\u884c'), (2, '\u4e2d\u65ad'), (3, '\u5df2\u7ecf\u5b8c\u6210')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='thetype',
            field=models.IntegerField(verbose_name='\u9879\u76ee\u7c7b\u578b', choices=[(0, '\u4f1a\u5c55\u8bc4\u4f30'), (1, '\u5a92\u4f53\u8bc4\u4f30')]),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='allow_domains',
            field=models.CharField(max_length=256, verbose_name='\u5141\u8bb8\u57df\u540d'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='allow_url',
            field=models.CharField(max_length=256, verbose_name='\u5141\u8bb8url'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='body_xpath',
            field=models.CharField(max_length=256, verbose_name='\u5185\u5bb9Xpath'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='enable',
            field=models.IntegerField(default=1, verbose_name='\u542f\u7528\u6807\u8bb0', choices=[(0, '\u672a\u542f\u7528'), (1, '\u542f\u7528')]),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='extract_from',
            field=models.CharField(max_length=256, verbose_name='\u63d0\u53d6\u89c4\u5219'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='next_page',
            field=models.CharField(max_length=256, verbose_name='\u4e0b\u4e00\u9875Xpath'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='publish_time_xpath',
            field=models.CharField(max_length=256, verbose_name='\u516c\u5e03\u65f6\u95f4Xpath'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='source_site_xpath',
            field=models.CharField(max_length=256, verbose_name='\u6e90\u7ad9Xpath'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='start_urls',
            field=models.CharField(max_length=256, verbose_name='\u5f00\u59cb\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='ruler',
            name='title_xpath',
            field=models.CharField(max_length=256, verbose_name='\u6807\u9898Xpath'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='domain',
            field=models.CharField(max_length=256, verbose_name='\u57df\u540d'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='flag',
            field=models.SmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(1, '\u81ea\u52a8\u83b7\u5f97'), (2, '\u5f85\u7ea0\u6b63'), (3, '\u5df2\u786e\u5b9a')]),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='ip',
            field=models.IntegerField(verbose_name='IP\u91cf'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='locate',
            field=models.CharField(max_length=256, verbose_name='\u5c5e\u5730'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='name',
            field=models.CharField(max_length=256, verbose_name='\u5c5e\u6027\u540d'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='nature',
            field=models.SmallIntegerField(default=3, verbose_name='\u5c5e\u6027', choices=[(1, '\u5b98\u7f51'), (2, '\u4f1a\u5c55\u7c7b\u7f51'), (3, '\u666e\u901a\u7f51'), (4, '\u5927\u578b\u65b0\u95fb\u7f51')]),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='pv',
            field=models.IntegerField(verbose_name='PV\u91cf'),
        ),
    ]
