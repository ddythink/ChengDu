#coding=utf-8
from .database_config import databasenames,usernames,passwords
import MySQLdb
from django.http import HttpResponse
import json
from .models import Project,Siteproperty,Article
from .models import Report,Everyyear,Citydata
from . import  execute_by_sql


import datetime

#得到控制串的api调用函数
def control(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for result in results:
            response_data['control'] = result.control


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到会展项目table的api调用函数
def table(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

            projects = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid)

            for project in projects:

                response_data['name'] = project.pname
                response_data['category'] = project.exhibition_type
                response_data['gross_area'] = project.area
                response_data['start_date'] = str(project.start_time)
                response_data['stop_date'] = str(project.end_time)
                response_data['industry'] = project.industry
                response_data['company_from'] = '本地'+str(project.com_num_local)+'，外省'+str(project.com_num_provin)+'，国外'+str(project.com_num_broad)
                response_data['viewer_from'] = '本地'+str(project.peo_num_local)+'，外省'+str(project.peo_num_provin)+'，国外'+str(project.peo_num_broad)


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到会展项目雷达图的api调用函数
def radar(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)
            #找到项目信息
            projects = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid)
            for project in projects:

                start_date = str(project.start_time)
                stop_date = project.end_time
                new_stop_date = str(stop_date+datetime.timedelta(days=1))

        #找到文章总数
        totalnum=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s' % pid)

        #获取媒体总数
        sql_media = 'select * from spacider_siteproperty where id in (select site_property_id from spacider_article where project_id=%s)' % pid
        medianum=execute_by_sql.exe_sql(sql_media)
        #获取会前宣传总数
        sql_bifore = 'select * from spacider_article where project_id=%s and publish_time<"%s"' % (pid,start_date)
        beforenum=execute_by_sql.exe_sql(sql_bifore)
        #获取会前宣传总数

        afternum=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s and publish_time>="%s"' % (pid,new_stop_date))

        response_data['media'] = medianum
        response_data['article_sum'] = totalnum
        response_data['before_sum'] = beforenum
        response_data['after_sum'] = afternum


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")

#得到会展项目趋势图的api调用函数
def trend_report(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

        #找到文章总数
        str1= '%Y-%m-%d'
        sql_media = 'select  DATE_FORMAT(publish_time,"%s") pub_time,count(1) as numb from spacider_article where project_id=%s GROUP BY pub_time' % (str1,pid)
        #print "执行的sql语句是：",sql_media

        try:

            conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
            cur=conn.cursor()
            conn.select_db(databasenames)
            #获取数量
            cur.execute(sql_media)

            results = cur.fetchall()
            for result in results:
                response_data = dict()
                response_data["date"]=result[0]
                response_data["num"]=result[1]
                response_list.append(response_data)
                # response_data["date"]='ss'
                # response_data["num"]='ss'

            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error,e:
            print e

    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")


#得到会展项目趋势图的api调用函数
def time_media(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

        #找到发布文章的网站列表，并按照时间排序
        str1= '%Y-%m-%d'
        sql_site_time = 'SELECT DATE_FORMAT(aaaa.publish_time,"%s") pub_time,   aaaa.site_property_id, spacider_siteproperty.site_name FROM  (select  publish_time, site_property_id  from spacider_article  where project_id=%s  ORDER BY publish_time) aaaa , spacider_siteproperty WHERE aaaa.site_property_id = spacider_siteproperty.id GROUP BY aaaa.site_property_id ORDER BY aaaa.publish_time ' % (str1,pid)
        #print "执行的sql语句是：",sql_media

        try:

            conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
            cur=conn.cursor()
            conn.select_db(databasenames)
            #获取数量
            cur.execute(sql_site_time)

            results = cur.fetchall()
            for result in results:
                response_data = dict()
                response_data["Media"]=result[2]
                response_data["Reprinted_time"]=result[0]
                response_list.append(response_data)

            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error,e:
            print e

    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")




#得到会展项目媒体及其影响力的api调用函数
def media_impact(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

        sql_site_ip = 'select  site_name, ip, pv  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) GROUP BY ip ORDER BY ip DESC limit 0,10' % pid

        try:

            conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
            cur=conn.cursor()
            conn.select_db(databasenames)
            #获取数量
            cur.execute(sql_site_ip)

            results = cur.fetchall()
            for result in results:
                print result[2]
                response_data = dict()
                response_data["Media"]=result[0]
                response_data["IP"]=result[1]
                response_data["PV"]=result[2]
                response_list.append(response_data)
                # response_data["date"]='ss'
                # response_data["num"]='ss'

            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error,e:
            print e

    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")





#得到会展项目媒体及其位置的api调用函数
def media_location(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

        sql_site_locate = 'select  locate, count(1)  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) GROUP BY locate ' % pid

        try:

            conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
            cur=conn.cursor()
            conn.select_db(databasenames)
            #获取数量
            cur.execute(sql_site_locate)

            results = cur.fetchall()
            for result in results:
                response_data = dict()
                response_data["name"]=result[0]
                response_data["value"]=result[1]

                response_list.append(response_data)
                # response_data["date"]='ss'
                # response_data["num"]='ss'

            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error,e:
            print e

    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")




#得到会展项目媒体及其结构的api调用函数
def media_structure(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)

        #会展类媒体数量
        specialnum=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 2' % pid)

        #获取媒体总数
        ordinarynum=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 3' % pid)
        #获取会前宣传总数
        newsnum=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 4' % pid)
        #获取会前宣传总数

        governmentnum=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 1' % pid)

        response_data1 = dict()
        response_data1["value"]=specialnum
        response_data1["name"]='会展专业媒体'
        response_list.append(response_data1)
        response_data2 = dict()
        response_data2["value"]=ordinarynum
        response_data2["name"]='普通媒体'
        response_list.append(response_data2)
        response_data3 = dict()
        response_data3["value"]=newsnum
        response_data3["name"]='大型新闻媒体'
        response_list.append(response_data3)
        response_data4 = dict()
        response_data4["value"]=governmentnum
        response_data4["name"]='政府官网'
        response_list.append(response_data4)
    except Report.DoesNotExist:
        response_list['msg'] = '未找到'
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")



