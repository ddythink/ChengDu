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

if __name__=="__main__":
    print "OK"