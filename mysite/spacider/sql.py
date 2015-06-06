from django.db import connection

def count_article_by_project_id(pid):
    cursor = connection.cursor()

    exeSQL = 'SELECT  CAST( spacider_article.publish_time AS DATE ) , COUNT( * ) AS asum FROM spacider_relationap, spacider_article ' \
             'WHERE project_id ' \
             '' \
             '=%d AND article_id = spacider_article.id GROUP BY CAST( spacider_article.publish_time AS DATE ) ORDER BY spacider_article.publish_time' % pid


    print exeSQL

    cursor.execute(exeSQL)
    row = cursor.fetchall()

    return row

def count_article_site(pid):
    cursor = connection.cursor()
    exeSQL = 'SELECT * FROM (SELECT site_property_id, COUNT( * ) FROM  spacider_relationas AS ras,  spacider_article AS a,  ' \
             'spacider_project AS p,  spacider_relationap AS rap WHERE p.id = rap.project_id AND rap.article_id = ' \
             'a.id AND a.id = ras.article_id AND p.id =%d GROUP BY site_property_id) AS t JOIN  spacider_siteproperty AS site ON t.site_property_id = site.id' % pid

    print exeSQL
    cursor.execute(exeSQL)
    row = cursor.fetchall()
    return row

def return_sum(pid):
    return len(count_article_site(pid))

def count_publish_time_by_project_id(pid):
    cursor = connection.cursor()
    exeSQL = 'SELECT publish_time, site.name FROM spacider_relationas AS ras, spacider_article AS a, ' \
             'spacider_project AS p, spacider_relationap AS rap, spacider_siteproperty AS site WHERE p.id = ' \
             'rap.project_id AND ras.site_property_id = site.id AND rap.article_id = a.id AND a.id = ras.article_id ' \
             'AND p.id =%d GROUP BY site.name' % pid

    print exeSQL
    cursor.execute(exeSQL)
    row = cursor.fetchall()
    return row

def ip_PV(pid):
    cursor = connection.cursor()
    exeSQL = 'SELECT site.name, site.ip, site.pv FROM spacider_relationas AS ras, spacider_article AS a, ' \
             'spacider_project AS p, spacider_relationap AS rap, spacider_siteproperty AS site WHERE p.id = ' \
             'rap.project_id AND ras.site_property_id = site.id AND rap.article_id = a.id AND a.id = ras.article_id ' \
             'AND p.id =%d GROUP BY site.name ORDER BY site.ip DESC , site.pv DESC ' % pid
    print exeSQL
    cursor.execute(exeSQL)
    row = cursor.fetchall()
    return row

if __name__=="__main__":
    print "OK"