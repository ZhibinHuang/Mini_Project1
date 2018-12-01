#!/usr/bin/env python
# encoding: utf-8
#Author - Zhibin Huang
import tweepy #https://github.com/tweepy/tweepy
import io 
import os
import re
import urllib.request

def getpic(filename_appendix):
    #Twitter API credentials
    consumer_key = "your key"
    consumer_secret = "your key"
    access_key = "your key"
    access_secret = "your key"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #get all urls in doc json
    s=open("tweet.json","r").read()
    results=re.findall("(?isu)(http\://[a-zA-Z0-9\.\?/&\=\:]+)",s)
    open("urls.txt","w").write("\r\n".join(results))

    #find all pictures' url which contain .jpg
    with open("urls.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
        #print(lines)
    with open("picurl.txt","w",encoding="utf-8") as f_w:
        for line in lines:
            if "jpg" in line:
                {}
            else:
                continue
            f_w.write(line)

    #drop the same urls because in json doc, it only differ in http & https
    rFile = open("picurl.txt", "r")
    wFile = open("single.txt", "w")
    lines = rFile.readlines()
    rFile.close()
    s = set()
    for i in lines:
        s.add(i)
    for i in s:
        wFile.write(i)
    wFile.close()

    #download the pics from twitter
    n = str(filename_appendix)
    name = 'twipic' + n;
    file_path = '/Users/huang/Documents/tw/%s' %name
    file_name = 0
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        with open("single.txt","r",encoding="utf-8") as f_w:
            lines = f_w.readlines()
            #print(len(lines))
            x = 0
            for line in lines:
                file_suffix = '.jpg'
                file_name = '%02d'%(x+1)
                filename1 = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
                #filename1 = '%02d.jpg' %x
                print(filename1)
                urllib.request.urlretrieve(line,filename=filename1)
                x = x+1
    except IOError as e:
        print("IOError")
    except Exception as e:
        print("Exception")

if __name__ == '__main__':
    getpic(0)
