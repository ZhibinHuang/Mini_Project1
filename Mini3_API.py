#!/usr/bin/env python
# encoding: utf-8
#Author - Zhibin Huang

import GoogleVision
import mysql
import mongodb
from flask import Flask
import flask_restful
import sys
import os

def Api():
    app = Flask(__name__)
    api = flask_restful.Api(app)

    class HelloWorld(flask_restful.Resource):
        def get(self):
            return {'hello': 'world'}
    api.add_resource(HelloWorld, '/')
    app.run(host='0.0.0.0')

def create_video():
    os.system("./ffmpeg -y -r 1 -i twipic0/%02d.jpg -vcodec libx264 -r 1 -t 15 -b 200k test0.mp4")

if __name__ == '__main__':
    #Api()
    print('Please inter your name and the twitter id you want to download ')
    print('')
    if len(sys.argv) >= 3:
        a = sys.argv[1]
        b = sys.argv[2]
    elif len(sys.argv) == 2:
        a = sys.argv[1]
        b = input("Please inter the twitter name ")
    elif len(sys.argv) == 1:
        a = input("Yourname: ")
        b = input("Twittername: ")
    print('')
    username = a
    twname = b
    filename_appendix = 0

    GoogleVision.googlevision(username,twname,filename_appendix)
    print('Information stored successfully in the databases.\n')

    str = input("Do you want to search for some keyword in the databases ? (Y/N): ")
    if(str == 'Y'or str == 'y'):
        key = input("Please input the keyword: ")
        mysql.search('twitter',key)
        print('')
        mongodb.search('twitter',key)
    else:
        print('')
        print('Thank you for using! ')