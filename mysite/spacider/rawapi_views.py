# -*- coding:utf-8 -*-

#from bson import json_util
import json, datetime
from .models import Project,Article
from django.core import serializers
#from django.http import Http404
from django.http import HttpResponse
from django.utils import timezone
from .models import RelationAP,Project
#from django.forms.models import model_to_dict
#from django.http import JsonResponse

def project_by_name(request, pname):
    response_data = dict()
    try:
        project = Project.objects.get(pname=pname)
        response_data['pid'] = project.id
    except Project.DoesNotExist:
        response_data['msg'] = u"未找到"
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")

def article_sum_by_project_id(request, pid):
    response_data = dict()
    try:
        project = Project.objects.get(pk=pid)
        response_data['id'] = pid
        response_data['pname'] = project.pname
        response_data['article_sum'] = project.relationap_set.count()
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")

def after_display_by_project_id(request, pid):
    response_data = dict()
    try:
        project = Project.objects.get(pk=pid)
        response_data['id'] = pid
        response_data['pname'] = project.pname
        start_time = project.start_time
        response_data['p_start_time'] = str(start_time)
        relations = project.relationap_set.all() # 所有的相关关系
        SER_ARTICLES = [serializers.serialize("json", [relation.article, ],
        fields=('title','url','pk','spider_from','publish_time')) for relation in relations if
                        relation.article.publish_time > start_time]

        for i, item in enumerate(SER_ARTICLES):
            response_data['article_'+str(i+1)] = json.loads(item)
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")




# reference
def article_by_id(request, aid):
    response_data = dict()
    try:
        article = Article.objects.get(pk=aid)
        #response_data['msg'] = u'找到啦'
        data = serializers.serialize("json", [article, ], fields=('title','url','pk','spider_from'))
        response_data = json.dumps({
            "first_data":json.loads(data),
            "oosss":"sb"
        })
        return HttpResponse(response_data,content_type="application/json",charset="utf-8")
        #response_data['article'] = data
        #response_data['article'] = model_to_dict(article)
    except Article.DoesNotExist:
        response_data['msg'] = u"未找到"
    # data = serializers.serialize("json", [Article.objects.get(pk=aid),], fields=('title','url','pk','spider_from'))
    # response_data['article'] = data
    #return HttpResponse(json.dumps(response_data, default=json_util.default), content_type="application/json")






