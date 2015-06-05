# -*- coding: utf-8 -*-
from django.utils import timezone

import json,datetime
from django.http import HttpResponse

def rador_graph(request, id):
    id = int(id)
    re_data = dict()
    re_data['article_num'] = id * 2
    re_data['before_num'] = id * 4
    re_data['atfter_num'] = id * 9
    re_data['media_num'] = id * 1

    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def trend_report(request, id):
    id = int(id)
    a_sum = 100 + id
    re_data = dict()
    today = datetime.date.today()
    for i in range(id):
        re_data[str(today+datetime.timedelta(i))] = a_sum - i * 10

    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def trend_report(request, id):
    id = int(id)
    a_sum = 100 + id
    re_data = dict()
    today = datetime.date.today()
    for i in range(id):
        re_data[str(today+datetime.timedelta(i))] = a_sum - i * 10

    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def convert(request, id):
    re_data = dict()
    tmp = dict()
    dsp = dict()
    tmp['media']  = u"中国新闻网"
    tmp['reprinted_time'] = str(datetime.date.today())
    dsp['media'] = u'搜狐新闻'
    dsp['reprinted_time'] = str(datetime.date.today() + datetime.timedelta(int(id)))
    for i in range(int(id)):
        if i % 2 == 0:
            re_data[i] = tmp
        else:
            re_data[i] = dsp

    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def media_location(request, id):
    re_data = [u'北京', u'河南', u'吉林',u'河北',u'江苏']
    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def media_structure(request, id):
    re_data = dict()
    tmp = dict()
    tm = dict()
    tp=dict()
    tmp[u'中国新闻网'] = "10%"
    re_data[1] = tmp
    tm[u'搜狐新闻'] = "60%"
    re_data[2] = tm
    tp[u'中国会展网'] = "30%"
    re_data[3] = tp
    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")

def media_impact(request, id):
    tmp = dict()
    tsp = dict()
    re_data = dict()
    tmp['ip'] = 10000
    tmp['pv'] = 200000
    tmp['media'] = u'中国新闻网'
    tsp['ip'] = 1000
    tsp['pv'] = 2000
    tsp['media'] = u"搜狐新闻"
    for i in range(10):
        if i % 2==0:
            re_data[i] = tmp
        else:
            re_data[i] = tsp
    return HttpResponse(json.dumps(re_data), content_type="application/json",charset="utf-8")






