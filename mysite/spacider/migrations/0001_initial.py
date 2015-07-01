# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('url', models.CharField(max_length=256, verbose_name='\u6587\u7ae0URL')),
                ('body', models.TextField(null=True, verbose_name='\u6587\u7ae0\u5185\u5bb9', blank=True)),
                ('publish_time', models.DateTimeField(verbose_name='\u6587\u7ae0\u516c\u5e03\u65f6\u95f4')),
                ('source_site', models.CharField(max_length=256, null=True, verbose_name='\u6e90\u7ad9', blank=True)),
                ('source_site_url', models.CharField(max_length=256, null=True, blank=True)),
                ('source_url', models.CharField(max_length=256, null=True, blank=True)),
                ('spider_from', models.IntegerField(default=0, verbose_name='\u6765\u6e90', choices=[(1, b'wuchong'), (2, b'junpeng'), (0, b'no set')])),
                ('crawler_time', models.DateTimeField(auto_now_add=True, verbose_name='\u722c\u53d6\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Citydata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4, verbose_name='\u5e74\u5ea6')),
                ('city', models.CharField(max_length=25, verbose_name='\u57ce\u5e02\u540d')),
                ('total_area', models.FloatField(verbose_name='\u603b\u5c55\u51fa\u9762\u79ef')),
                ('hardware', models.FloatField(verbose_name='\u573a\u9986\u9762\u79ef')),
                ('exhibition_num', models.IntegerField(verbose_name='\u529e\u5c55\u603b\u6570\u91cf')),
                ('over_3w', models.IntegerField(verbose_name='3\u4e07\u5e73\u65b9\u7c73\u4ee5\u4e0a\u4e2a\u6570')),
                ('over_3w_area', models.IntegerField(verbose_name='3\u4e07\u7c73\u4ee5\u4e0a\u5c55\u89c8\u9762\u79ef\u548c')),
            ],
            options={
                'verbose_name': '\u57ce\u5e02\u6570\u636e',
                'verbose_name_plural': '\u57ce\u5e02\u6570\u636e',
            },
        ),
        migrations.CreateModel(
            name='Everyyear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4, verbose_name='\u5e74\u5ea6')),
                ('exhibition', models.IntegerField(verbose_name='\u91cd\u5927\u4f1a\u5c55\u6d3b\u52a8\u4e2a\u6570')),
                ('show', models.IntegerField(verbose_name='\u529e\u5c55\u603b\u6570\u91cf')),
                ('nati_confe', models.IntegerField(verbose_name='\u56fd\u9645\u4f1a\u8bae\u4e2a\u6570')),
                ('total_area', models.FloatField(verbose_name='\u5c55\u89c8\u603b\u9762\u79ef')),
                ('nati_exhibi', models.FloatField(verbose_name='\u56fd\u9645\u6027\u5c55\u89c8\u9762\u79ef')),
                ('peo_num', models.FloatField(verbose_name='\u53c2\u52a0\u4f1a\u5c55\u603b\u4eba\u6570')),
                ('outsiders', models.FloatField(verbose_name='\u5916\u5730\u4eba')),
                ('direct_income', models.FloatField(verbose_name='\u76f4\u63a5\u6536\u5165')),
                ('total_income', models.FloatField(verbose_name='\u7efc\u5408\u6536\u5165')),
                ('job', models.IntegerField(verbose_name='\u5e26\u52a8\u5c31\u4e1a\u5c97\u4f4d')),
                ('sold', models.FloatField(verbose_name='\u5546\u54c1\u6210\u4ea4')),
                ('invest_agree', models.FloatField(verbose_name='\u6295\u8d44\u534f\u8bae\u91d1\u989d')),
            ],
            options={
                'verbose_name': '\u5386\u5e74\u72b6\u51b5',
                'verbose_name_plural': '\u5386\u5e74\u72b6\u51b5',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=256, verbose_name='\u9879\u76ee\u540d')),
                ('keywords', models.CharField(max_length=256, verbose_name='\u5173\u952e\u5b57')),
                ('locate', models.IntegerField(default=0, verbose_name='\u4f1a\u5c55\u5c5e\u5730', choices=[(0, '\u6210\u90fd'), (1, '\u91cd\u5e86'), (2, '\u4e0a\u6d77')])),
                ('project_type', models.IntegerField(verbose_name='\u9879\u76ee\u7c7b\u578b', choices=[(0, '\u4f1a\u5c55\u8bc4\u4f30'), (1, '\u5a92\u4f53\u8bc4\u4f30')])),
                ('exhibition_type', models.CharField(max_length=256, verbose_name='\u4f1a\u5c55\u7c7b\u578b')),
                ('start_time', models.DateField(null=True, verbose_name='\u4f1a\u5c55\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_time', models.DateField(null=True, verbose_name='\u4f1a\u5c55\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('period', models.DateTimeField(null=True, verbose_name='\u9879\u76ee\u8fd0\u884c\u65f6\u95f4', blank=True)),
                ('com_num_local', models.IntegerField(default=0, verbose_name='\u672c\u5730\u4f01\u4e1a\u6570\u91cf')),
                ('com_num_provin', models.IntegerField(default=0, verbose_name='\u5916\u7701\u4f01\u4e1a\u6570\u91cf')),
                ('com_num_broad', models.IntegerField(default=0, verbose_name='\u56fd\u5916\u4f01\u4e1a\u6570\u91cf')),
                ('peo_num_local', models.IntegerField(default=0, verbose_name='\u672c\u5730\u89c2\u4f17\u6570\u91cf')),
                ('peo_num_provin', models.IntegerField(default=0, verbose_name='\u5916\u7701\u89c2\u4f17\u6570\u91cf')),
                ('peo_num_broad', models.IntegerField(default=0, verbose_name='\u56fd\u5916\u89c2\u4f17\u6570\u91cf')),
                ('area', models.IntegerField(default=0, verbose_name='\u6bdb\u9762\u79ef')),
                ('industry', models.CharField(max_length=256, null=True, verbose_name='\u6d89\u53ca\u4e3b\u8981\u884c\u4e1a', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u9879\u76ee\u72b6\u6001', choices=[(0, '\u5df2\u521b\u5efa'), (1, '\u6b63\u5728\u8fd0\u884c'), (2, '\u4e2d\u65ad'), (3, '\u5df2\u7ecf\u5b8c\u6210')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u9879\u76ee\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pids', models.CharField(max_length=256, verbose_name='\u9879\u76eeID\u4e32')),
                ('rname', models.CharField(max_length=256, verbose_name='\u8bc4\u4f30\u540d')),
                ('control', models.CharField(max_length=256, verbose_name='\u63a7\u5236\u5b57\u7b26\u4e32')),
                ('report_type', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u7c7b\u578b', choices=[(0, '\u4f1a\u5c55\u62a5\u544a8\u56fe'), (1, '\u5a92\u4f53\u62a5\u544a6\u56fe'), (2, '\u76f8\u540c\u5730\u533a4\u56fe'), (3, '\u4e0d\u540c\u5730\u533a4\u56fe'), (4, '\u57ce\u5e02\u5bf9\u6bd46\u56fe')])),
                ('zero', models.TextField(null=True, verbose_name='\u5f00\u5934\u63cf\u8ff0', blank=True)),
                ('one', models.TextField(null=True, verbose_name='\u89c4\u6a21\u8bc4\u4f30', blank=True)),
                ('two', models.TextField(null=True, verbose_name='\u96f7\u8fbe\u56fe\u63cf\u8ff0', blank=True)),
                ('three', models.TextField(null=True, verbose_name='\u62a5\u9053\u8d8b\u52bf\u63cf\u8ff0', blank=True)),
                ('four', models.TextField(null=True, verbose_name='\u53d1\u5e03\u8d8b\u52bf\u63cf\u8ff0', blank=True)),
                ('five', models.TextField(null=True, verbose_name='\u8f6c\u53d1\u63cf\u8ff0', blank=True)),
                ('six', models.TextField(null=True, verbose_name='\u4f20\u64ad\u5f71\u54cd\u529b\u63cf\u8ff0', blank=True)),
                ('seven', models.TextField(null=True, verbose_name='\u5a92\u4f53\u5730\u57df\u5206\u5e03\u63cf\u8ff0', blank=True)),
                ('eight', models.TextField(null=True, verbose_name='\u5a92\u4f53\u7ed3\u6784\u7ec4\u6210\u63cf\u8ff0', blank=True)),
            ],
            options={
                'verbose_name': '\u62a5\u544a',
                'verbose_name_plural': '\u62a5\u544a',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u89c4\u5219\u540d')),
                ('allow_domains', models.CharField(max_length=256, verbose_name='\u5141\u8bb8\u57df\u540d')),
                ('start_urls', models.CharField(max_length=256, verbose_name='\u5f00\u59cb\u94fe\u63a5')),
                ('next_page', models.CharField(max_length=256, verbose_name='\u4e0b\u4e00\u9875Xpath')),
                ('allow_url', models.CharField(max_length=256, verbose_name='\u5141\u8bb8url')),
                ('extract_from', models.CharField(max_length=256, verbose_name='\u63d0\u53d6\u89c4\u5219')),
                ('title_xpath', models.CharField(max_length=256, verbose_name='\u6807\u9898Xpath')),
                ('body_xpath', models.CharField(max_length=256, verbose_name='\u5185\u5bb9Xpath')),
                ('publish_time_xpath', models.CharField(max_length=256, verbose_name='\u516c\u5e03\u65f6\u95f4Xpath')),
                ('source_site_xpath', models.CharField(max_length=256, verbose_name='\u6e90\u7ad9Xpath')),
                ('enable', models.IntegerField(default=1, verbose_name='\u542f\u7528\u6807\u8bb0', choices=[(0, '\u672a\u542f\u7528'), (1, '\u542f\u7528')])),
            ],
            options={
                'verbose_name': '\u89c4\u5219',
                'verbose_name_plural': '  \u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='Siteproperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=256, verbose_name='\u57df\u540d')),
                ('site_name', models.CharField(max_length=256, verbose_name='\u7f51\u7ad9\u540d')),
                ('locate', models.CharField(max_length=256, verbose_name='\u6240\u5c5e\u5730')),
                ('nature', models.SmallIntegerField(default=3, verbose_name='\u7f51\u7ad9\u7c7b\u522b', choices=[(1, '\u5b98\u7f51'), (2, '\u4f1a\u5c55\u7c7b\u7f51'), (3, '\u666e\u901a\u7f51'), (4, '\u5927\u578b\u65b0\u95fb\u7f51')])),
                ('ip', models.IntegerField(verbose_name='IP\u91cf')),
                ('pv', models.IntegerField(verbose_name='PV\u91cf')),
                ('flag', models.SmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(1, '\u81ea\u52a8\u83b7\u5f97'), (2, '\u5f85\u7ea0\u6b63'), (3, '\u5df2\u786e\u5b9a')])),
            ],
            options={
                'verbose_name': '\u5c5e\u6027',
                'verbose_name_plural': '\u5c5e\u6027',
            },
        ),
        migrations.AddField(
            model_name='rule',
            name='attr',
            field=models.ForeignKey(related_name='rule_siteproverty', to='spacider.Siteproperty'),
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(related_name='pro_articles', to='spacider.Project'),
        ),
        migrations.AddField(
            model_name='article',
            name='site_property',
            field=models.ForeignKey(related_name='site_articles', to='spacider.Siteproperty'),
        ),
    ]
