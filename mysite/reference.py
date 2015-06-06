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