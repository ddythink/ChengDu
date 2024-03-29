from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views as aviews
from . import views
from . import rawapi_views
from . import tapi

router = routers.SimpleRouter()
router.register(r'article', aviews.ArticleViewSet)
router.register(r'rule', aviews.RulerViewSet)
#router.register(r'infotrack', aviews.InfotrackViewSet)
router.register(r'project', aviews.ProjectViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^generate_report/$', views.generate_report, name='generate_report'),
    url(r'^report/(?P<pk>[0-9]+)/$', views.report, name='chengdu-report'),
    url(r'^compare/report/(?P<pk>[0-9]+)/$', views.returnReport),
    url(r'^api/', include(router.urls)),
    url(r'^api/project/(?P<pk>[0-9]+)/$', aviews.project_detail),
    #url(r'^api/trend/(?P<project_id>[0-9]+)/$', aviews.infotrack_trend),
    #url(r'^api/infotrack/(?P<pk>[0-9]+)/$', aviews.InfotrackDetail.as_view()),
    #-------------------------------------------------------------------------------
    url(r'^api/project/(?P<pname>[\w]+)', rawapi_views.project_by_name),
    url(r'^api/article/sum/(?P<pid>[\d]+)/$', rawapi_views.article_sum_by_project_id),
    url(r'^api/article/trend/(?P<pid>[\d]+)/$', rawapi_views.article_trend_display_by_project_id),
    url(r'^api/radior/(?P<pid>[\d]+)/$', rawapi_views.radior),
    url(r'^api/trend_report/(?P<pid>[\d]+)/$', rawapi_views.article_trend_display_by_project_id),
    url(r'^api/convert/(?P<pid>[\d]+)/$', rawapi_views.convert),
    url(r'^api/media_location/(?P<id>[\d]+)/$', tapi.media_location),
    url(r'^api/media_structure/(?P<pid>[\d]+)/$', rawapi_views.media_structure),
    url(r'^api/media_impact/(?P<pid>[\d]+)/$', rawapi_views.media_impact)
]

urlpatterns = format_suffix_patterns(urlpatterns)
