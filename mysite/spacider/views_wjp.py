#coding=utf-8
from .database_config import databasenames,usernames,passwords
import MySQLdb
from django.http import HttpResponse
import json
from .models import Project,Siteproperty,Article
from .models import Report,Everyyear,Citydata
from . import  execute_by_sql


import datetime

#得到控制串的api调用函数，各种类型评估通用
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

#得到会展项目（媒体项目）趋势图的api调用函数
def trend_report(request,result_id):
    response_list=list()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            pid = int(pids)


        str1= '%Y-%m-%d'
        sql_media = 'select  DATE_FORMAT(publish_time,"%s") pub_time,count(1) as numb from spacider_article where project_id=%s GROUP BY pub_time' % (str1,pid)
        #print "执行的sql语句是：",sql_media

        try:

            conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
            cur=conn.cursor()
            conn.select_db(databasenames)

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


#得到会展项目（媒体项目）媒体转发时间图的api调用函数
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




#得到会展项目（媒体项目）媒体及其影响力的api调用函数
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





#得到会展项目（媒体项目）媒体及其位置的api调用函数
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




#得到会展项目（媒体项目）媒体及其结构的api调用函数
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

#-----------------------------------------------------------------------------------------------------------

#得到成都地区会展项目对比的雷达图api调用函数
def same_radar(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])
            #找到项目信息
            projects1 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid1)
            for project1 in projects1:
                p1_name = project1.pname
                com_num_local1 = project1.com_num_local
                com_num_provin1 = project1.com_num_provin
                com_num_broad1 = project1.com_num_broad
                p1_company_num = com_num_local1+com_num_provin1+com_num_broad1
                peo_num_local1 = project1.peo_num_local
                peo_num_provin1 = project1.peo_num_provin
                peo_num_broad1 = project1.peo_num_broad
                p1_viewer_num = peo_num_local1+peo_num_provin1+peo_num_broad1

                p1_area_num = project1.area

                start_date1 = project1.start_time
                p1_start_date = str(start_date1)
                stop_date1 = project1.end_time
                p1_stop_date = str(stop_date1)
                p1_time_num = stop_date1-start_date1
                print "sssssssssgggggggggggg",str(p1_time_num)

                response_data['p1_name'] = p1_name
                response_data['p1_company_num'] = p1_company_num
                response_data['p1_viewer_num'] = p1_viewer_num
                response_data['p1_area_num'] = p1_area_num
                response_data['p1_time_num'] = p1_time_num
                response_data['p1_start_date'] = p1_start_date
                response_data['p1_stop_date'] = p1_stop_date

            projects2 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid2)
            for project2 in projects2:
                p2_name = project2.pname
                com_num_local2 = project2.com_num_local
                com_num_provin2 = project2.com_num_provin
                com_num_broad2 = project2.com_num_broad
                p2_company_num = com_num_local2+com_num_provin2+com_num_broad2
                peo_num_local2 = project2.peo_num_local
                peo_num_provin2 = project2.peo_num_provin
                peo_num_broad2 = project2.peo_num_broad
                p2_viewer_num = peo_num_local2+peo_num_provin2+peo_num_broad2

                p2_area_num = project2.area

                start_date2 = project2.start_time
                p2_start_date = str(start_date2)
                stop_date2 = project2.end_time
                p2_stop_date = str(stop_date2)
                p2_time_num = stop_date2-start_date2
                print "sssssssssgggggggggggg",str(p1_time_num)

                response_data['p2_name'] = p2_name
                response_data['p2_company_num'] = p2_company_num
                response_data['p2_viewer_num'] = p2_viewer_num
                response_data['p2_area_num'] = p2_area_num
                response_data['p2_time_num'] = p2_time_num
                response_data['p2_start_date'] = p2_start_date
                response_data['p2_stop_date'] = p2_stop_date

    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到成都地区会展项目对比的趋势图api调用函数
def same_trend_report(request,result_id):
    response_list=dict()
    try:

        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])


            response_list1=list()
            str1= '%Y-%m-%d'
            sql_trend1 = 'select  DATE_FORMAT(publish_time,"%s") pub_time,count(1) as numb from spacider_article where project_id=%s GROUP BY pub_time' % (str1,pid1)
            #print "执行的sql语句是：",sql_media

            try:

                conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
                cur=conn.cursor()
                conn.select_db(databasenames)

                cur.execute(sql_trend1)

                results1 = cur.fetchall()
                for result1 in results1:
                    response_data1 = dict()
                    response_data1["date"]=result1[0]
                    response_data1["num"]=result1[1]
                    response_list1.append(response_data1)


                conn.commit()
                cur.close()
                conn.close()

            except MySQLdb.Error,e:
                print e


            response_list2=list()
            str2= '%Y-%m-%d'
            sql_trend2 = 'select  DATE_FORMAT(publish_time,"%s") pub_time,count(1) as numb from spacider_article where project_id=%s GROUP BY pub_time' % (str2,pid2)
            #print "执行的sql语句是：",sql_media

            try:

                conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
                cur=conn.cursor()
                conn.select_db(databasenames)

                cur.execute(sql_trend2)

                results2 = cur.fetchall()
                for result2 in results2:
                    response_data2 = dict()
                    response_data2["date"]=result2[0]
                    response_data2["num"]=result2[1]
                    response_list2.append(response_data2)


                conn.commit()
                cur.close()
                conn.close()

            except MySQLdb.Error,e:
                print e

            response_list={"P1":response_list1,"P2":response_list2}


    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")


#得到成都地区会展项目对比的媒体转发时间图的api调用函数
def same_time_media(request,result_id):
    response_list=dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])


            response_list1=list()
            #找到发布文章的网站列表，并按照时间排序
            str1= '%Y-%m-%d'
            sql_site_time1 = 'SELECT DATE_FORMAT(aaaa.publish_time,"%s") pub_time,   aaaa.site_property_id, spacider_siteproperty.site_name FROM  (select  publish_time, site_property_id  from spacider_article  where project_id=%s  ORDER BY publish_time) aaaa , spacider_siteproperty WHERE aaaa.site_property_id = spacider_siteproperty.id GROUP BY aaaa.site_property_id ORDER BY aaaa.publish_time ' % (str1,pid1)
            #print "执行的sql语句是：",sql_media

            try:

                conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
                cur=conn.cursor()
                conn.select_db(databasenames)

                cur.execute(sql_site_time1)

                results1 = cur.fetchall()
                for result1 in results1:
                    response_data1 = dict()
                    response_data1["Media"]=result1[2]
                    response_data1["Reprinted_time"]=result1[0]
                    response_list1.append(response_data1)

                conn.commit()
                cur.close()
                conn.close()

            except MySQLdb.Error,e:
                print e


            response_list2 = list()
            #找到发布文章的网站列表，并按照时间排序
            str2= '%Y-%m-%d'
            sql_site_time2 = 'SELECT DATE_FORMAT(aaaa.publish_time,"%s") pub_time,   aaaa.site_property_id, spacider_siteproperty.site_name FROM  (select  publish_time, site_property_id  from spacider_article  where project_id=%s  ORDER BY publish_time) aaaa , spacider_siteproperty WHERE aaaa.site_property_id = spacider_siteproperty.id GROUP BY aaaa.site_property_id ORDER BY aaaa.publish_time ' % (str2,pid2)
            #print "执行的sql语句是：",sql_media

            try:

                conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
                cur=conn.cursor()
                conn.select_db(databasenames)

                cur.execute(sql_site_time2)

                results2 = cur.fetchall()
                for result2 in results2:
                    response_data2 = dict()
                    response_data2["Media"]=result2[2]
                    response_data2["Reprinted_time"]=result2[0]
                    response_list2.append(response_data2)

                conn.commit()
                cur.close()
                conn.close()

            except MySQLdb.Error,e:
                print e


            response_list={"P1":response_list1,"P2":response_list2}

    except Report.DoesNotExist:
        response_list = ['未找到']
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")


#得到成都地区(不同地区)会展项目对比的媒体及其结构的api调用函数
def same_media_structure(request,result_id):
    response_list=dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])

            response_list1=list()

            specialnum1=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 2' % pid1)
            ordinarynum1=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 3' % pid1)
            newsnum1=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 4' % pid1)
            governmentnum1=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 1' % pid1)

            response_data11 = dict()
            response_data11["value"]=specialnum1
            response_data11["name"]='会展专业媒体'
            response_list1.append(response_data11)
            response_data12 = dict()
            response_data12["value"]=ordinarynum1
            response_data12["name"]='普通媒体'
            response_list1.append(response_data12)
            response_data13 = dict()
            response_data13["value"]=newsnum1
            response_data13["name"]='大型新闻媒体'
            response_list1.append(response_data13)
            response_data14 = dict()
            response_data14["value"]=governmentnum1
            response_data14["name"]='政府官网'
            response_list1.append(response_data14)



            response_list2=list()

            specialnum2=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 2' % pid2)
            ordinarynum2=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 3' % pid2)
            newsnum2=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 4' % pid2)
            governmentnum2=execute_by_sql.exe_sql('select *  from spacider_siteproperty where id  in (select  site_property_id  from spacider_article  where project_id=%s) and nature = 1' % pid2)

            response_data21 = dict()
            response_data21["value"]=specialnum2
            response_data21["name"]='会展专业媒体'
            response_list2.append(response_data21)
            response_data22 = dict()
            response_data22["value"]=ordinarynum2
            response_data22["name"]='普通媒体'
            response_list2.append(response_data22)
            response_data23 = dict()
            response_data23["value"]=newsnum2
            response_data23["name"]='大型新闻媒体'
            response_list2.append(response_data23)
            response_data24 = dict()
            response_data24["value"]=governmentnum2
            response_data24["name"]='政府官网'
            response_list2.append(response_data24)


            response_list = {"P1":response_list1,"P2":response_list2}


    except Report.DoesNotExist:
        response_list['msg'] = '未找到'
    return HttpResponse(json.dumps(response_list), content_type="application/json",charset="utf-8")


#得到不同地区会展项目对比的表格api调用函数
def diff_table(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])
            #找到项目信息
            projects1 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid1)
            for project1 in projects1:
                p1_name = project1.pname
                p1_gross_area = project1.area
                p1_industry = project1.industry

                com_num_local1 = str(project1.com_num_local)
                com_num_provin1 = str(project1.com_num_provin)
                p1_company = "本省"+com_num_local1+"，外省"+com_num_provin1

                peo_num_local1 = project1.peo_num_local
                peo_num_provin1 = project1.peo_num_provin
                p1_viewer_num = "本省"+peo_num_local1+"，外省"+peo_num_provin1

                response_data['p1_name'] = p1_name
                response_data['p1_gross_area'] = p1_gross_area
                response_data['p1_industry'] = p1_industry
                response_data['p1_company'] = p1_company
                response_data['p1_viewer_num'] = p1_viewer_num

            projects2 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid2)
            for project2 in projects2:
                p2_name = project2.pname
                p2_gross_area = project2.area
                p2_industry = project2.industry

                com_num_local2 = str(project2.com_num_local)
                com_num_provin2 = str(project2.com_num_provin)
                p2_company = "本省"+com_num_local2+"，外省"+com_num_provin2

                peo_num_local2 = project2.peo_num_local
                peo_num_provin2 = project2.peo_num_provin
                p2_viewer_num = "本省"+peo_num_local2+"，外省"+peo_num_provin2

                response_data['p2_name'] = p2_name
                response_data['p2_gross_area'] = p2_gross_area
                response_data['p2_industry'] = p2_industry
                response_data['p2_company'] = p2_company
                response_data['p2_viewer_num'] = p2_viewer_num

    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到不同地区会展项目对比的柱状图api调用函数
def diff_num(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])

            #找到文章总数
            totalnum1=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s' % pid1)
            #获取媒体总数
            sql_media1 = 'select * from spacider_siteproperty where id in (select site_property_id from spacider_article where project_id=%s)' % pid1
            medianum1=execute_by_sql.exe_sql(sql_media1)

            response_data['p1_article_num'] = totalnum1
            response_data['p1_media_num'] = medianum1


            #找到文章总数
            totalnum2=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s' % pid2)
            #获取媒体总数
            sql_media2 = 'select * from spacider_siteproperty where id in (select site_property_id from spacider_article where project_id=%s)' % pid2
            medianum2=execute_by_sql.exe_sql(sql_media2)

            response_data['p2_article_num'] = totalnum2
            response_data['p2_media_num'] = medianum2



    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")




#得到不同地区会展项目对比的会议前中后柱状图api调用函数
def diff_seminate(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            list_pids = pids.split("|")
            pid1 = int(list_pids[0])
            pid2 = int(list_pids[1])


            #找到项目信息
            projects1 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid1)
            for project1 in projects1:

                start_date1 = str(project1.start_time)
                stop_date1 = project1.end_time
                new_stop_date1 = str(stop_date1+datetime.timedelta(days=1))

            #找到文章总数
            totalnum1=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s' % pid1)

            #获取会前宣传总数
            sql_bifore1 = 'select * from spacider_article where project_id=%s and publish_time<"%s"' % (pid1,start_date1)
            beforenum1=execute_by_sql.exe_sql(sql_bifore1)
            #获取会前宣传总数

            afternum1=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s and publish_time>="%s"' % (pid1,new_stop_date1))

            response_data['p1_before_sum'] = beforenum1
            response_data['p1_during_sum'] = totalnum1-beforenum1-afternum1
            response_data['p1_after_sum'] = afternum1

            #找到项目信息
            projects2 = Project.objects.raw("SELECT * FROM spacider_project WHERE id = %s" % pid2)
            for project2 in projects2:

                start_date2 = str(project2.start_time)
                stop_date2 = project2.end_time
                new_stop_date2 = str(stop_date2+datetime.timedelta(days=1))

            #找到文章总数
            totalnum2=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s' % pid2)

            #获取会前宣传总数
            sql_bifore2 = 'select * from spacider_article where project_id=%s and publish_time<"%s"' % (pid2,start_date2)
            beforenum2=execute_by_sql.exe_sql(sql_bifore2)
            #获取会前宣传总数

            afternum2=execute_by_sql.exe_sql('select * from spacider_article where project_id=%s and publish_time>="%s"' % (pid2,new_stop_date2))

            response_data['p2_before_sum'] = beforenum2
            response_data['p2_during_sum'] = totalnum2-beforenum2-afternum2
            response_data['p2_after_sum'] = afternum2


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'
    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到9城市对比的柱状图1api调用函数
def ex_area(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.total_area
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.total_area
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.total_area
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.total_area
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.total_area
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.total_area
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.total_area
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.total_area
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.total_area
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")


#得到9城市对比的柱状图2 api调用函数
def venue_area(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.hardware
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.hardware
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.hardware
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.hardware
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.hardware
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.hardware
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.hardware
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.hardware
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.hardware
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")


#得到9城市对比的柱状图3 api调用函数
def ex_num(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.exhibition_num
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.exhibition_num
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.exhibition_num
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.exhibition_num
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.exhibition_num
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.exhibition_num
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.exhibition_num
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.exhibition_num
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.exhibition_num
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到9城市对比的柱状图4 api调用函数
def confe_num(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.nati_confe
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.nati_confe
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.nati_confe
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.nati_confe
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.nati_confe
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.nati_confe
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.nati_confe
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.nati_confe
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.nati_confe
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到9城市对比的柱状图5 api调用函数
def w3_num(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.over_3w
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.over_3w
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.over_3w
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.over_3w
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.over_3w
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.over_3w
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.over_3w
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.over_3w
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.over_3w
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")





#得到9城市对比的柱状图6 api调用函数
def w3_area(request,result_id):
    response_data = dict()
    try:
        results = Report.objects.raw("SELECT * FROM spacider_report WHERE id = %s" % result_id)
        for res in results:
            pids = res.pids
            #2014年中提取出2014
            year_int = int(filter(str.isdigit, pids))

            ninecitys = Citydata.objects.raw("SELECT * FROM spacider_citydata WHERE year = %s" % year_int)
            for ninecity in ninecitys:
                city = ninecity.city
                if city.find("成都") != -1:
                    response_data['CD'] = ninecity.over_3w_area
                elif city.find("广州") != -1:
                    response_data['GZ'] = ninecity.over_3w_area
                elif city.find("上海") != -1:
                    response_data['SH'] = ninecity.over_3w_area
                elif city.find("北京") != -1:
                    response_data['BJ'] = ninecity.over_3w_area
                elif city.find("深圳") != -1:
                    response_data['SZ'] = ninecity.over_3w_area
                elif city.find("天津") != -1:
                    response_data['TJ'] = ninecity.over_3w_area
                elif city.find("重庆") != -1:
                    response_data['CQ'] = ninecity.over_3w_area
                elif city.find("武汉") != -1:
                    response_data['WH'] = ninecity.over_3w_area
                elif city.find("南京") != -1:
                    response_data['NJ'] = ninecity.over_3w_area
                else:
                    pass


    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")



#得到9城市对比的柱状图6 api调用函数
def years(request,year1,year2):
    response_data = dict()
    try:
        everyyears1 = Everyyear.objects.raw("SELECT * FROM spacider_everyyear WHERE year = %s" % year1)
        for everyyear1 in everyyears1:
            year1_data = everyyear1.year
            p1_year = str(year1_data)+"年"
            p1_bigP = everyyear1.exhibition
            p1_events = everyyear1.show_num
            p1_interconfer = everyyear1.nati_confe
            p1_area = everyyear1.total_area
            p1_area_inter = everyyear1.nati_exhibi
            p1_viewer = everyyear1.peo_num
            p1_veiwer_out = everyyear1.outsiders
            p1_dincome = everyyear1.direct_income
            p1_allincome = everyyear1.total_income
            p1_jobs = everyyear1.job
            p1_deal = everyyear1.sold
            p1_invest = everyyear1.invest_agree


        everyyears2 = Everyyear.objects.raw("SELECT * FROM spacider_everyyear WHERE year = %s" % year2)
        for everyyear2 in everyyears2:
            year2_data = everyyear2.year
            p2_year = str(year2_data)+"年"
            p2_bigP = everyyear2.exhibition
            p2_events = everyyear2.show_num
            p2_interconfer = everyyear2.nati_confe
            p2_area = everyyear2.total_area
            p2_area_inter = everyyear2.nati_exhibi
            p2_viewer = everyyear2.peo_num
            p2_veiwer_out = everyyear2.outsiders
            p2_dincome = everyyear2.direct_income
            p2_allincome = everyyear2.total_income
            p2_jobs = everyyear2.job
            p2_deal = everyyear2.sold
            p2_invest = everyyear2.invest_agree




        in_bigP = str((float(p2_bigP)/p1_bigP-1)*100)+"%"

        in_events = str((float(p2_events)/p1_events-1)*100)+"%"
        in_interconfer = str((float(p2_interconfer)/p1_interconfer-1)*100)+"%"
        in_area = str((float(p2_area)/p1_area-1)*100)+"%"
        in_area_inter = str((float(p2_area_inter)/p1_area_inter-1)*100)+"%"
        in_viewer = str((float(p2_viewer)/p1_viewer-1)*100)+"%"
        in_veiwer_out = str((float(p2_veiwer_out)/p1_veiwer_out-1)*100)+"%"
        in_dincome = str((float(p2_dincome)/p1_dincome-1)*100)+"%"
        in_allincome = str((float(p2_allincome)/p1_allincome-1)*100)+"%"
        in_jobs = str((float(p2_jobs)/p1_jobs-1)*100)+"%"
        in_deal = str((float(p2_deal)/p1_deal-1)*100)+"%"
        in_invest = str((float(p2_invest)/p1_invest-1)*100)+"%"

        response_data['p1_year'] = p1_year
        response_data['p1_bigP'] = p1_bigP
        response_data['p1_events'] = p1_events
        response_data['p1_interconfer'] = p1_interconfer
        response_data['p1_area'] = p1_area
        response_data['p1_area_inter'] = p1_area_inter
        response_data['p1_viewer'] = p1_viewer
        response_data['p1_veiwer_out'] = p1_veiwer_out
        response_data['p1_dincome'] = p1_dincome
        response_data['p1_allincome'] = p1_allincome
        response_data['p1_jobs'] = p1_jobs
        response_data['p1_deal'] = p1_deal
        response_data['p1_invest'] = p1_invest

        response_data['p2_year'] = p2_year
        response_data['p2_bigP'] = p2_bigP
        response_data['p2_events'] = p2_events
        response_data['p2_interconfer'] = p2_interconfer
        response_data['p2_area'] = p2_area
        response_data['p2_area_inter'] = p2_area_inter
        response_data['p2_viewer'] = p2_viewer
        response_data['p2_veiwer_out'] = p2_veiwer_out
        response_data['p2_dincome'] = p2_dincome
        response_data['p2_allincome'] = p2_allincome
        response_data['p2_jobs'] = p2_jobs
        response_data['p2_deal'] = p2_deal
        response_data['p2_invest'] = p2_invest


        response_data['increase'] = "增长"
        response_data['in_bigP'] = in_bigP
        response_data['in_events'] = in_events
        response_data['in_interconfer'] = in_interconfer
        response_data['in_area'] = in_area
        response_data['in_area_inter'] = in_area_inter
        response_data['in_viewer'] = in_viewer
        response_data['in_veiwer_out'] = in_veiwer_out
        response_data['in_dincome'] = in_dincome
        response_data['in_allincome'] = in_allincome
        response_data['in_jobs'] = in_jobs
        response_data['in_deal'] = in_deal
        response_data['in_invest'] = in_invest

    except Report.DoesNotExist:
        response_data['msg'] = '未找到'

    return HttpResponse(json.dumps(response_data), content_type="application/json",charset="utf-8")








