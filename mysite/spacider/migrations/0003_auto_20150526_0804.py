# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacider', '0002_auto_20150526_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationAP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationAS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='project',
        ),
        migrations.RemoveField(
            model_name='article',
            name='site_property',
        ),
        migrations.AddField(
            model_name='relationas',
            name='article',
            field=models.OneToOneField(to='spacider.Article'),
        ),
        migrations.AddField(
            model_name='relationas',
            name='site_property',
            field=models.OneToOneField(to='spacider.Siteproperty'),
        ),
        migrations.AddField(
            model_name='relationap',
            name='article',
            field=models.OneToOneField(to='spacider.Article'),
        ),
        migrations.AddField(
            model_name='relationap',
            name='project',
            field=models.OneToOneField(to='spacider.Project'),
        ),
    ]
