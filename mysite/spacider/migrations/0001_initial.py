# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('allow_domains', models.CharField(max_length=256)),
                ('start_urls', models.CharField(max_length=256)),
                ('next_page', models.CharField(max_length=256)),
                ('allow_url', models.CharField(max_length=256)),
                ('extract_from', models.CharField(max_length=256)),
                ('title_xpath', models.CharField(max_length=256)),
                ('body_xpath', models.CharField(max_length=256)),
                ('publish_time_xpath', models.CharField(max_length=256)),
                ('source_site_xpath', models.CharField(max_length=256)),
                ('enable', models.IntegerField(default=0)),
            ],
        ),
    ]
