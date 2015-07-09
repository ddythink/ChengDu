#coding=utf-8
from .database_config import databasenames,usernames,passwords
import MySQLdb

def exe_sql(sql):
    num = 0
    try:

        conn=MySQLdb.connect(host='localhost',user=usernames,passwd=passwords,port=3306,charset="utf8")
        cur=conn.cursor()
        conn.select_db(databasenames)
        #获取数量
        num=cur.execute(sql)


        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error,e:
        print e

    return num