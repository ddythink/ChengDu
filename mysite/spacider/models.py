# -*- coding:utf-8 _*_

from django.db import models
from .config import YEAR
from .config import CITY_LOCATE
from .config import REPORT_TYPE
from .config import PROJECT_TYPE
from .config import PROJECT_STATUS
from .config import SPIDER_SRC
from .config import NATURE
from .config import FLAG
from .config import USE

# Create your models here.


class Siteproperty(models.Model):

    domain = models.CharField(u'域名', max_length=256)
    site_name = models.CharField(u'网站名', max_length=256)
    locate = models.CharField(u'所属地名', max_length=256)
    nature = models.SmallIntegerField(u'网站类别', choices=NATURE)
    ip = models.IntegerField(u'IP量')
    pv = models.IntegerField(u'PV量')
    flag = models.SmallIntegerField(u'数据状态', choices=FLAG)

    def __unicode__(self):
        return self.site_name+" "+self.domain

    class Meta:
        verbose_name = u'属性'
        verbose_name_plural=u'属性'


class Rule(models.Model):

    name = models.CharField(u"规则名", max_length=50)
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
    attr = models.ForeignKey(Siteproperty, related_name="rule_siteproverty") # 规则增加属性

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'规则'
        verbose_name_plural=u'  规则'


class Project(models.Model):

    pname = models.CharField(u'项目名', max_length=256)
    keywords =models.CharField(u'关键字', max_length=256)
    project_type = models.IntegerField(u'项目类型', choices=PROJECT_TYPE)
    locate = models.IntegerField(u'会展属地', choices=CITY_LOCATE, default=0)
    exhibition_type = models.CharField(u'会展类型', max_length=256, blank=True, null=True)
    start_time = models.DateField(u'会展开始时间', blank=True, null=True)
    end_time  = models.DateField(u'会展结束时间', blank=True, null=True)
    area = models.IntegerField(u'毛面积', blank=True, null=True)
    com_num_local = models.IntegerField(u'本地企业数量', default=0, blank=True, null=True)
    com_num_provin = models.IntegerField(u'外省企业数量', default=0, blank=True, null=True)
    com_num_broad = models.IntegerField(u'国外企业数量', default=0, blank=True, null=True)
    peo_num_local = models.IntegerField(u'本地观众数量', default=0, blank=True, null=True)
    peo_num_provin = models.IntegerField(u'外省观众数量', default=0, blank=True, null=True)
    peo_num_broad = models.IntegerField(u'国外观众数量', default=0, blank=True, null=True)
    industry =  models.CharField(u'涉及主要行业', blank=True, null=True, max_length=256)
    period = models.IntegerField(u'项目运行时间')
    status = models.IntegerField(u'项目状态', default=0, choices=PROJECT_STATUS)
    create_time = models.DateTimeField(u'项目创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.pname

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural=u'项目'


class Article(models.Model):

    title = models.CharField(u'文章标题', max_length=256)
    url = models.CharField(u'文章URL', max_length=256)
    body = models.TextField(u'文章内容', blank=True, null=True)
    publish_time = models.DateTimeField(u'文章公布时间')
    source_site = models.CharField(u'源站', max_length=256, blank=True, null=True)
    source_site_url = models.CharField(max_length=256, blank=True, null=True)
    source_url = models.CharField(max_length=256, blank=True, null=True)
    spider_from = models.IntegerField(u'来源', choices=SPIDER_SRC)
    crawler_time = models.DateTimeField(u'爬取时间')
    project = models.ForeignKey(Project, related_name="pro_articles")
    site_property = models.ForeignKey(Siteproperty, related_name="site_articles")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural=u'文章'

class Report(models.Model):

    pids = models.CharField(u'项目ID串', max_length=256)
    rname = models.CharField(u'评估名', max_length=256)
    control = models.CharField(u'控制字符串', max_length=256)
    report_type = models.SmallIntegerField(u'展示类型', default=0, choices=REPORT_TYPE)
    zero = models.TextField(u'开头描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    one = models.TextField(u'规模评估', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    two = models.TextField(u'雷达图描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    three = models.TextField(u'报道趋势描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    four = models.TextField(u'发布趋势描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    five = models.TextField(u'转发描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    six = models.TextField(u'传播影响力描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    seven = models.TextField(u'媒体地域分布描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")
    eight = models.TextField(u'媒体结构组成描述', blank=True, null=True, default=u"这里用于输入报告的描述信息")

    class Meta:
        verbose_name = u'报告'
        verbose_name_plural=u'报告'

class Citydata(models.Model):

    year = models.SmallIntegerField(u'年份', choices=YEAR)
    city = models.CharField(u'城市名', max_length=25)
    total_area = models.FloatField(u'总展出面积')
    hardware = models.FloatField(u'场馆面积')
    exhibition_num = models.IntegerField(u'办展总数量')
    over_3w = models.IntegerField(u'3万平方米以上个数')
    over_3w_area = models.FloatField(u'3万米以上展览面积和')

    class Meta:
        verbose_name = u'城市数据'
        verbose_name_plural=u'城市数据'


class Everyyear(models.Model):

  year = models.SmallIntegerField(u'年份', choices=YEAR)
  exhibition = models.IntegerField(u'重大会展活动个数')
  show_num = models.IntegerField(u'办展总数量')
  nati_confe = models.IntegerField(u'国际会议个数')
  total_area = models.FloatField(u'展览总面积')
  nati_exhibi = models.FloatField(u'国际性展览面积')
  peo_num = models.FloatField(u'参加会展总人数')
  outsiders  = models.FloatField(u'外地人')
  direct_income = models.FloatField(u'直接收入')
  total_income = models.FloatField(u'综合收入')
  job = models.IntegerField(u'带动就业岗位')
  sold = models.FloatField(u'商品成交')
  invest_agree = models.FloatField(u'投资协议金额')

  class Meta:
        verbose_name = u'历年状况'
        verbose_name_plural=u'历年状况'


# class Infotrack(models.Model):

#     SPIDER_SRC=(
#             (1,'wuchong'),
#             (2,'junpeng'),
#             (0,'no set'),
#             )
#     class Meta:
#         verbose_name = u'爬虫动态'
#         verbose_name_plural=u'爬虫动态'

#     project = models.ForeignKey(Project, related_name='infotrack_ids')
#     add_num = models.IntegerField(u'增加数目', default=0)
#     sum_total = models.IntegerField(u'总共数目')
#     run_date    = models.DateTimeField(u'运行日期')
#     spend_time = models.IntegerField(u'花费时间', blank=True,null=True)
#     spider_from = models.IntegerField(u'爬取来源', default=0, choices=SPIDER_SRC)
