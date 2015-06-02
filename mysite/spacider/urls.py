from django.conf.urls import url, include
from rest_framework import routers
from . import api_views as aviews
from . import views

router = routers.SimpleRouter()
router.register(r'article', aviews.ArticleViewSet)
router.register(r'rule', aviews.RulerViewSet)
router.register(r'infotrack', aviews.InfotrackViewSet)
router.register(r'project', aviews.ProjectViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api/project/(?P<pk>[0-9]+)/$', aviews.project_detail)
]
