# -*- coding:utf-8 -*-
import json, datetime
from .models import Project,Article
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from .models import RelationAP,Project
from .sql import *

def radior(request, pid):
    response_data = dict()
    try:
        project = Project.objects.get(pk=pid)
        response_data['article_sum'] = project.relationap_set.count()
        articles = count_article_by_project_id(int(pid))
        start_date = project.start_time.date()
        end_date   = project.end_time.date()
        before_sum = 0
        after_sum  = 0
        for item in articles:
            if item[0] < start_date:
                before_sum += item[1]
            elif item[0] > end_date:
                after_sum += item[1]
            else:
                pass
        response_data['before_sum'] = before_sum
        response_data['after_sum'] = after_sum
        response_data['media'] = return_sum(int(pid))
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")


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


def media_structure(request, pid):
    response_data = dict()
    try:
        rows = count_article_site(int(pid))
        csum = 0
        for item in rows:
            csum += item[1]
        for j in rows:
            response_data[j[4]] = '{0:.2%}'.format(float(j[1]) / float(csum))
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")

def convert(request, pid):
    response_data = dict()
    tmp = list()
    try:
        rows = count_publish_time_by_project_id(int(pid))
        response_data = dict([(item[1], str(item[0].date())) for item in rows])
        for item in rows:
            tmp.append({'Media':item[1],
                        'Reprinted_time':str(item[0].date())})
        tmp.sort(key=lambda x:x['Reprinted_time'])
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(tmp), content_type="application/json", charset="utf-8")

def media_impact(request, pid):
    response_data = dict()
    tmp = list()
    try:
        rows = ip_PV(int(pid))
        for item in rows:
            tmp.append({'Media':item[0],
                        'IP':item[1],
                        'PV':item[2]})
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
        return HttpResponse(json.dumps(response_data), content_type="application/json", charset="utf-8")
    return HttpResponse(json.dumps(tmp), content_type="application/json", charset="utf-8")



def article_trend_display_by_project_id(request, pid):
    response_data = dict()
    arti_summy = dict()
    try:
        project = Project.objects.get(pk=pid)
        response_data['id'] = pid
        response_data['pname'] = project.pname
        response_data['start_time'] = str(project.start_time)
        response_data['end_time'] = str(project.end_time)
        response_data['article_sum'] = project.relationap_set.count()
        artiles = dict(count_article_by_project_id(int(pid)))
        for key, value in artiles.iteritems():
            arti_summy[str(key)] = value
        response_data['artciles'] = arti_summy
    except Project.DoesNotExist:
        response_data['msg'] = u'未找到'
    return HttpResponse(json.dumps(response_data, sort_keys=True), content_type="application/json",charset="utf-8")



def before_display_by_project_id(request, pid):
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







