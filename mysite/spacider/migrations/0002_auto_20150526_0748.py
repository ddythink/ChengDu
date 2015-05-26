# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('publish_time', models.DateTimeField()),
                ('source_site', models.CharField(max_length=256)),
                ('source_site_url', models.CharField(max_length=256)),
                ('source_url', models.CharField(max_length=256)),
                ('spider_from', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=256)),
                ('keywords', models.CharField(max_length=256)),
                ('thetype', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('final_time', models.DateTimeField()),
                ('other', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Siteproperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('locate', models.CharField(max_length=256)),
                ('nature', models.SmallIntegerField()),
                ('ip', models.IntegerField()),
                ('pv', models.IntegerField()),
                ('flag', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(to='spacider.Project'),
        ),
        migrations.AddField(
            model_name='article',
            name='site_property',
            field=models.OneToOneField(to='spacider.Siteproperty'),
        ),
    ]
