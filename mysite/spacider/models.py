# -*- coding:utf-8 _*_

from django.db import models

# Create your models here.

class Siteproperty(models.Model):
    class Meta:
        verbose_name = u'属性'
        verbose_name_plural=u'属性'
    NATURE = ((1,u"官网"),
              (2,u"会展类网"),
              (3,u"普通网"),
              (4,u"大型新闻网"))
    FLAG = ((1,u'自动获得'),
            (2,u"待纠正"),
            (3,u"已确定"))
    domain = models.CharField(u'域名', max_length=256)
    name = models.CharField(u'属性名', max_length=256)
    locate = models.CharField(u'属地', max_length=256)
    nature = models.SmallIntegerField(u'属性', default=3, choices=NATURE)
    ip = models.IntegerField(u'IP量')
    pv = models.IntegerField(u'PV量')
    flag = models.SmallIntegerField(u'数据状态', default=1, choices=FLAG)

    def __unicode__(self):
        return self.name+" "+self.domain



class Ruler(models.Model):

    class Meta:
        verbose_name = u'规则'
        verbose_name_plural=u'  规则'

    USE = (
        (0, u'未启用'),
        (1, u'启用')
    )
    name = models.CharField(u"规则名",max_length=50)
    allow_domains = models.CharField(u'允许域名', max_length=256)
    start_urls = models.CharField(u'开始链接', max_length=256)
    next_page = models.CharField(u'下一页Xpath', max_length=256)
    allow_url =  models.CharField(u'允许url', max_length=256)
    extract_from =  models.CharField(u'提取规则', max_length=256)
    title_xpath =  models.CharField(u'标题Xpath', max_length=256)
    body_xpath =  models.CharField(u'内容Xpath', max_length=256)
    publish_time_xpath =  models.CharField(u'公布时间Xpath', max_length=256)
    source_site_xpath =  models.CharField(u'源站Xpath', max_length=256)
    enable = models.IntegerField(u'启用标记', default=1, choices=USE)
    attr = models.ForeignKey(Siteproperty) # 规则增加属性

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
    pname = models.CharField(u'项目名', max_length=256)
    keywords =models.CharField(u'关键字', max_length=256)
    thetype = models.IntegerField(u'项目类型', choices=THETYPE)
    start_time = models.DateTimeField(u'会展开始时间', blank=True, null=True)
    end_time  = models.DateTimeField(u'会展结束时间', blank=True, null=True)
    final_time = models.DateTimeField(u'项目结束时间', blank=True, null=True)
    other  = models.CharField(u'其他', max_length=256, blank=True, null=True)
    status = models.IntegerField(u'项目状态', default=0, choices=STATUS)
    create_time = models.DateTimeField(u'项目创建时间', auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.pname+":"+self.STATUS[self.status][1]

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural=u'项目'

class Article(models.Model):
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural=u' 文章'

    SPIDER_SRC=(
            (1,'wuchong'),
            (2,'junpeng'),
            (0,'no set'),
            )
    #project = models.ForeignKey(Project)
    title = models.CharField(u'文章标题', max_length=256)
    url = models.CharField(u'文章URL', max_length=256)
    body = models.TextField(u'文章内容', blank=True, null=True)
    publish_time = models.DateTimeField(u'文章公布时间')
    source_site = models.CharField(u'源站', max_length=256, blank=True, null=True)
    source_site_url = models.CharField(max_length=256, blank=True, null=True)
    source_url = models.CharField(max_length=256, blank=True, null=True)
    #site_property = models.OneToOneField(Siteproperty)
    spider_from = models.IntegerField(u'来源', default=0, choices=SPIDER_SRC)
    crawler_time = models.DateTimeField(u'爬取时间', auto_now_add=True, blank=True)


    def __unicode__(self):
        return self.title


class RelationAP(models.Model):
    class Meta:
        verbose_name = u'文章与项目'
        verbose_name_plural=u'文章与项目'
    project = models.ForeignKey(Project)
    article = models.ForeignKey(Article)


class RelationAS(models.Model):
    class Meta:
        verbose_name = u'文章与属性'
        verbose_name_plural=u'文章与属性'
    article = models.ForeignKey(Article)
    site_property = models.ForeignKey(Siteproperty)

class Infotrack(models.Model):
    SPIDER_SRC=(
            (1,'wuchong'),
            (2,'junpeng'),
            (0,'no set'),
            )
    class Meta:
        verbose_name = u'爬虫动态'
        verbose_name_plural=u'爬虫动态'

    project = models.ForeignKey(Project, related_name='infotrack_ids')
    add_num = models.IntegerField(u'增加数目', default=0)
    sum_total = models.IntegerField(u'总共数目')
    run_date    = models.DateTimeField(u'运行日期')
    spend_time = models.IntegerField(u'花费时间', blank=True,null=True)
    spider_from = models.IntegerField(u'爬取来源', default=0, choices=SPIDER_SRC)
