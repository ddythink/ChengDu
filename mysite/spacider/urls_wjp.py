#coding=utf-8
__author__ = 'wujunpeng'
from . import views_wjp
from django.conf.urls import include, url

urlpatterns = [

    # 会展项目api
    url(r'^exhibition/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^exhibition/table/(?P<result_id>[0-9]+)/$', views_wjp.table, name='table'),
    url(r'^exhibition/radar/(?P<result_id>[0-9]+)/$', views_wjp.radar, name='radar'),
    url(r'^exhibition/trend_report/(?P<result_id>[0-9]+)/$', views_wjp.trend_report, name='trend_report'),
    url(r'^exhibition/time_media/(?P<result_id>[0-9]+)/$', views_wjp.time_media, name='time_media'),
    url(r'^exhibition/media_impact/(?P<result_id>[0-9]+)/$', views_wjp.media_impact, name='media_impact'),
    url(r'^exhibition/media_location/(?P<result_id>[0-9]+)/$', views_wjp.media_location, name='media_location'),
    url(r'^exhibition/media_structure/(?P<result_id>[0-9]+)/$', views_wjp.media_structure, name='media_structure'),

    # 媒体项目api
    url(r'^media/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^media/trend_report/(?P<result_id>[0-9]+)/$', views_wjp.trend_report, name='trend_report'),
    url(r'^media/time_media/(?P<result_id>[0-9]+)/$', views_wjp.time_media, name='time_media'),
    url(r'^media/media_impact/(?P<result_id>[0-9]+)/$', views_wjp.media_impact, name='media_impact'),
    url(r'^media/media_location/(?P<result_id>[0-9]+)/$', views_wjp.media_location, name='media_location'),
    url(r'^media/media_structure/(?P<result_id>[0-9]+)/$', views_wjp.media_structure, name='media_structure'),

    # 成都地区对比项目api
    url(r'^same_compare/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^same_compare/radar/(?P<result_id>[0-9]+)/$', views_wjp.same_radar, name='same_radar'),
    url(r'^same_compare/trend_report/(?P<result_id>[0-9]+)/$', views_wjp.same_trend_report, name='same_trend_report'),
    url(r'^same_compare/time_media/(?P<result_id>[0-9]+)/$', views_wjp.same_time_media, name='same_time_media'),
    url(r'^same_compare/media_structure/(?P<result_id>[0-9]+)/$', views_wjp.same_media_structure, name='same_media_structure'),


    # 不同地区对比项目api
    url(r'^diff_compare/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^diff_compare/table/(?P<result_id>[0-9]+)/$', views_wjp.diff_table, name='diff_table'),
    url(r'^diff_compare/num/(?P<result_id>[0-9]+)/$', views_wjp.diff_num, name='diff_num'),
    url(r'^diff_compare/media_structure/(?P<result_id>[0-9]+)/$', views_wjp.same_media_structure, name='same_media_structure'),
    url(r'^diff_compare/seminate/(?P<result_id>[0-9]+)/$', views_wjp.diff_seminate, name='diff_seminate'),


    # 成都与其他八个城市对比项目api
    url(r'^nine/control/(?P<result_id>[0-9]+)/$', views_wjp.control, name='control'),
    url(r'^nine/ex_area/(?P<result_id>[0-9]+)/$', views_wjp.ex_area, name='ex_area'),
    url(r'^nine/venue_area/(?P<result_id>[0-9]+)/$', views_wjp.venue_area, name='venue_area'),
    url(r'^nine/ex_num/(?P<result_id>[0-9]+)/$', views_wjp.ex_num, name='ex_num'),
    url(r'^nine/confe_num/(?P<result_id>[0-9]+)/$', views_wjp.confe_num, name='confe_num'),
    url(r'^nine/3w_num/(?P<result_id>[0-9]+)/$', views_wjp.w3_num, name='w3_num'),
    url(r'^nine/3w_area/(?P<result_id>[0-9]+)/$', views_wjp.w3_area, name='w3_area'),
    # 成都年度数据api
    url(r'^year/(?P<year1>[0-9]{4})|(?P<year2>[0-9]{4})/$', views_wjp.years, name='years'),



]