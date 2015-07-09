#coding=utf-8
__author__ = 'wujunpeng'
from . import views_wjp
from django.conf.urls import include, url

urlpatterns = [

    url(r'^exhibition/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^exhibition/table/(?P<result_id>[0-9]+)/$', views_wjp.table, name='table'),
    url(r'^exhibition/radar/(?P<result_id>[0-9]+)/$', views_wjp.radar, name='radar'),
    url(r'^exhibition/trend_report/(?P<result_id>[0-9]+)/$', views_wjp.trend_report, name='trend_report'),
    url(r'^exhibition/time_media/(?P<result_id>[0-9]+)/$', views_wjp.time_media, name='time_media'),
    url(r'^exhibition/media_impact/(?P<result_id>[0-9]+)/$', views_wjp.media_impact, name='media_impact'),
    url(r'^exhibition/media_location/(?P<result_id>[0-9]+)/$', views_wjp.media_location, name='media_location'),
    url(r'^exhibition/media_structure/(?P<result_id>[0-9]+)/$', views_wjp.media_structure, name='media_structure'),



]