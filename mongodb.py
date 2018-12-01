#!/usr/bin/env python
# encoding: utf-8
#Author - Zhibin Huang

import pymongo
import datetime
import os

def opt_mongodb(user,tablename,idd,twname,tag,twnum,phnum,phaddr,viaddr):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mini3"]
    collect = db[tablename]
    dblist = client.list_database_names()
    #if "mini3" in dblist:
        #print('mini3 database exist')
    #print(dblist)
    c_time = datetime.datetime.now()
    #d, twusername, tags, tweetnum, photonum, photoaddr, videoaddr, timenow
    mydict = {'username':user,'id': idd, 'twittername': twname, 'tags': tag, 'tweetnum':twnum, 'photonum':phnum, 'photoaddr':phaddr, \
              'videoaddr':viaddr,'time':c_time}

    x = collect.insert_one(mydict)

    collist = db. list_collection_names()
    #if "%s"%tablename in collist:
      #print("%s collection exist" %tablename)
    #print('')
    #quiry1 = {"tags":{"$in":"Gap"}}

def search(tablename,key):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mini3"]
    collect = db[tablename]
    quiry = {"tags": {"$regex": ".*%s.*" % key}}
    result = collect.find(quiry)
    result1 = collect.find_one(quiry)
    if(result1==None):
        print('Keyword %s is not found in collection %s (MongoDB)' %(key,tablename))
    else:
        print('Keyword %s founded in collection %s below (MongoDB):' %(key,tablename))
        for a in result:
            print(a)

if __name__ =='__main__':
    opt_mongodb('Josh','twitter',7,'twi','Gap',2,3,'cpan','dpan')
    search('twitter','basket')