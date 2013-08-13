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

import re
import requests
import redis
import logging
from bs4 import BeautifulSoup

class spider():
    def __init__(self, log_addr, log_format, log_lvl, ip, port, fre, keys):
        self.LOG_ADDRESS = log_addr
        self.LOG_FORMAT = log_format
        self.LOG_LEVEL = log_lvl
        self.REDIS_IP = ip  
        self.REDIS_PORT = port 
        self.REDIS_FREQUENCE = fre      
        self.SPIDER_KEYS = keys

    def init_log(self):
        logger = logging.getLogger() 
        handler = logging.FileHandler(self.LOG_ADDRESS)
        formatter = logging.Formatter(self.LOG_FORMAT) 
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(self.LOG_LEVEL)
        return logger

    def init_params(self):
        return (
                {
                    'host' : 'http://bbs.byr.cn',
                    'url'  : 'http://bbs.byr.cn/board/JobInfo',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/article/JobInfo/\d+$",
                },

                {
                    'host' : 'http://bbs.byr.cn',
                    'url'  : 'http://bbs.byr.cn/board/Job',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/article/Job/\d+$",
                },

                {
                    'host' : 'http://bbs.byr.cn',
                    'url'  : 'http://bbs.byr.cn/board/ParttimeJob',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/article/ParttimeJob/\d+$",
                },

                {
                    'host' : 'http://www.newsmth.net',
                    'url'  : 'http://www.newsmth.net/nForum/board/Career_Campus',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/nForum/article/Career_Campus/\d+$",
                },
            )

    def spider_cap(self, rs, host, url, headers, href):
        r = requests.get(url, headers = headers)
        #print url
        frs_soup = BeautifulSoup(r.text)
        frs_attrs = {
            'href' : re.compile(href),
            'title' : None,
            'target' : None,
        }
        frs_res =  frs_soup.findAll('a', frs_attrs)
        for line in frs_res:
            #去除置顶贴
            if line.parent.parent.get('class') == 'top':
                print "top jump"
                continue
            line['href'] = host + line['href']
            title = line.string
            if filter(lambda x: x in title, self.SPIDER_KEYS):
                #print line
                ars = rs.sadd('urls', line)

    def capture(self):
        logger = self.init_log()
        logger.info('spider start!')
        #print "spider start"

        rs = redis.Redis(host=self.REDIS_IP, port=self.REDIS_PORT)
        rs.incr('times')
        if int(rs.get('times')) >= self.REDIS_FREQUENCE:
            rs.flushall()
            
        #rs.set('test', "Test Successed!")#just for test redis

        params = self.init_params()

        for param in params :
            self.spider_cap(rs, param['host'], param['url'], param['headers'], param['href'])

        logger.info("spider finish!\n") 
        #print "spider finish"
