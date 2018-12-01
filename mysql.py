#!/usr/bin/env python
# encoding: utf-8
#Author - Zhibin Huang

import pymysql
import datetime
import re

def opt_mysql(user,tablename,idd,twname,tag,twnum,phnum,phaddr,viaddr):
    conn = pymysql.connect(host='localhost',port =3306,user='root',passwd='dear23132231',db ='mini3')
    cursor = conn.cursor()
    #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #print("Database version : %s " % data)
    b = tablename
    #drop_table = 'DROP TABLE IF EXISTS %s' %b
    #cursor.execute(drop_table)
    exist = table_exists(cursor,b)
    #print(exist)
    c_time = datetime.datetime.now()

    if(exist == 0):
        create_table = """create TABLE %s (
                          username CHAR(20),
                          id INT NOT NULL,
                          twittername CHAR(20),
                          tags CHAR(200) NOT NULL,
                          tweetnum INT,
                          photonum INT,
                          photoaddr CHAR(50),
                          videoaddr CHAR(50),
                          timenow CHAR(50))""" %b

        cursor.execute(create_table)
        conn.commit()


    sql = """INSERT INTO %s(username, id, twittername, tags, tweetnum, photonum, photoaddr, videoaddr, timenow)
             VALUES ('%s','%s','%s', '%s', %s,%s, '%s', '%s','%s')""" %(b,user,idd,twname,tag,twnum,phnum,phaddr,viaddr,c_time)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        # Rollback in case there is any error
        conn.rollback()

    #search(table_name,'basket')
    cursor.close()
    conn.close()
    #for i in range(idd):
        #print(c_time)

def table_exists(con,table_name):
    sql = "show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return 1
    else:
        return 0

def search(table_name, key):

    conn = pymysql.connect(host='localhost',port =3306,user='root',passwd='dear23132231',db ='mini3')
    cursor = conn.cursor()
    exist = table_exists(cursor, table_name)
    if(exist):
        newkey = '%' + key + '%'
        sql = "SELECT * FROM %s WHERE tags LIKE '%s' " % (table_name, newkey)
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.execute(sql)
            results = cursor.fetchall()
            if(result == None):
                print('')
                print("Keyword %s is not found in table %s (MySQL)"%(key,table_name))
            else:
                print("Keyword %s founded in table %s below (MySQL): "%(key,table_name))
            for row in results:
                user = row[0]
                id = row[1]
                twname = row[2]
                tag = row[3]
                tweetnum = row[4]
                photonum = row[5]
                photoaddr = row[6]
                videoaddr = row[7]
                stime = row[8]
                print("username = %s, id = %s, twittername = %s, tags = %s tweetnum = %s,photonum = %s, phoaddr = %s, videoaddr = %s, time = %s" \
                      %(user,id, twname, tag, tweetnum, photonum, photoaddr, videoaddr, stime))
        except:
            print("Error: unable to fecth data")
    else:
        print('Table does not exist')
    cursor.close()
    conn.close()

if __name__ =='__main__':
    opt_mysql('Josh','twitter',0,'Josh','GAP',7,17,'cpan','dpan')
    search('twitter', 'basket')