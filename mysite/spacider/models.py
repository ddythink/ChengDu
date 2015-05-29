# -*- coding:utf-8 _*_

from django.db import models

# Create your models here.

class Ruler(models.Model):

    class Meta:
        verbose_name = u'规则'
        verbose_name_plural=u'3. 规则'

    USE = (
        (0, u'未启用'),
        (1, u'启用')
    )
    name = models.CharField(max_length=50)
    allow_domains = models.CharField(max_length=256)
    start_urls = models.CharField(max_length=256)
    next_page = models.CharField(max_length=256)
    allow_url =  models.CharField(max_length=256)
    extract_from =  models.CharField(max_length=256)
    title_xpath =  models.CharField(max_length=256)
    body_xpath =  models.CharField(max_length=256)
    publish_time_xpath =  models.CharField(max_length=256)
    source_site_xpath =  models.CharField(max_length=256)
    enable = models.IntegerField(default=1, choices=USE)

    def __unicode__(self):
        return self.name + " "+self.allow_domains


class Project(models.Model):

    STATUS=(
            (0,u'已创建'),
            (1,u'正在运行'),
            (2,u'中断'),
            (3,u'已经完成'),
            )
    THETYPE=(
        (0, u'会展评估'),
        (1, u'媒体评估'),
    )
    pname = models.CharField(max_length=256)
    keywords =models.CharField(max_length=256)
    thetype = models.IntegerField(choices=THETYPE)
    start_time = models.DateTimeField()
    end_time  = models.DateTimeField()
    final_time = models.DateTimeField()
    other  = models.CharField(max_length=256)
    status = models.IntegerField(default=0, choices=STATUS)
    create_time = models.DateTimeField()

    def __unicode__(self):
        return self.pname+":"+self.STATUS[self.status][1]

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural=u'1. 项目'


class Siteproperty(models.Model):
    class Meta:
        verbose_name = u'专家库'
        verbose_name_plural=u'4. 专家库'
    domain = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    locate = models.CharField(max_length=256)
    nature = models.SmallIntegerField()
    ip = models.IntegerField()
    pv = models.IntegerField()
    flag = models.SmallIntegerField()

    def __unicode__(self):
        return self.name+" "+self.domain



class Article(models.Model):
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural=u'2. 文章'

    SPIDER_SRC=(
            (1,'wuchong'),
            (2,'junpeng'),
            (0,'no set'),
            )
    #project = models.ForeignKey(Project)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    body = models.TextField()
    publish_time = models.DateTimeField()
    source_site = models.CharField(max_length=256, blank=True, null=True)
    source_site_url = models.CharField(max_length=256, blank=True, null=True)
    source_url = models.CharField(max_length=256, blank=True, null=True)
    #site_property = models.OneToOneField(Siteproperty)
    spider_from = models.IntegerField(default=0, choices=SPIDER_SRC)
    crawler_time = models.DateTimeField(auto_now_add=True, blank=True)


    def __unicode__(self):
        return self.title


class RelationAP(models.Model):
    project = models.OneToOneField(Project)
    article = models.OneToOneField(Article)


class RelationAS(models.Model):
    article = models.OneToOneField(Article)
    site_property = models.OneToOneField(Siteproperty)
