#!/usr/local/python275/bin/python2.7
# -*- coding: utf-8 -*-
'''
#=============================================================================
#     FileName: main.py
#         Desc: 
#       Author: linjay
#        Email: linjayzhang326@gmail.com
#     HomePage: https://github.com/Linjay
#      Version: 0.0.2
#   LastChange: 2013-8-13 17:12:36
#      History:
#=============================================================================
'''
import redis
import time

class HtmlMaker():
    def __init__(self, ip, port, path):
        self.REDIS_IP = ip                                                  
        self.REDIS_PORT = port                                                       
        self.OUTPUT_PATH = path
        
    def makeHtml(self):
        f = open(self.OUTPUT_PATH,'w')
        #file write only, create new file if it not exist 

        print>>f, """<!DOCTYPE html>
                    <html>
                    <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                    <title>Welcome to spider!</title>
                    <style>
                    body {
                    width: 35em;
                    margin: 0 auto;
                }
                 a:visited { color: red; }
            </style>
            </head>
            <body>"""  #The HTML Code

        rs = redis.Redis(host=self.REDIS_IP, port=self.REDIS_PORT)
        #print rs.get("test")##just for test

        ret = rs.smembers("urls")
        for item in ret:
            print>>f, item
            print>>f, "<br/>"
        print>>f, "<br/><br/>Update at:" +time.ctime()+ "<br/>"
        print >> f, """</body></html>"""
        f.close()

