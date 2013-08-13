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
import time
import os
import sys
import threading
from spider import spider
from HtmlMaker import HtmlMaker
import logging
 
timer_interval=60       #update the data every 60 secs
micro_interval = 5      #s


class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.run_status = True
        global micro_interval
        self.MicroIntv = micro_interval
        self.OUTPUT_PATH = 'D:/Program Files/apache-tomcat-7.0.33/webapps/TestWebProject/rs.html'
                                #网页输出目录，应指向TOMCAT的WEBAPP存放目录
        self.REDIS_IP = '127.0.0.1'  #Redis的ip                                             #Redis的ip
        self.REDIS_PORT = 6379       #Redis的port
        self.LOG_ADDRESS = './spider_logging.txt'                   #日志文件地址
        self.LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'     #日志格式
        self.LOG_LEVEL = logging.DEBUG                                               #日志级别
        self.REDIS_FREQUENCE = 10                                                    #Redis清空的频率
        self.SPIDER_KEYS = ('Google','IBM','Intel','VMware', 'Adobe', u'广移', u'百度',u'阿里',u'腾讯',u'华为',u'联想',
                            u'工商银行',u'农业银行',u'建设银行',u'招商银行',u'航天',u'北京移动',u'北京电信')

    def run(self):
        global timer_interval
        htmlMaker = HtmlMaker(self.REDIS_IP, self.REDIS_PORT, self.OUTPUT_PATH)
        sp = spider(self.LOG_ADDRESS,self.LOG_FORMAT,self.LOG_LEVEL,self.REDIS_IP,self.REDIS_PORT,
                    self.REDIS_FREQUENCE,self.SPIDER_KEYS)
        while self.run_status:
            sp.capture()
            htmlMaker.makeHtml()
            self.sleep(timer_interval)

    def stop(self):
        self.run_status=False

    def sleep(self, inter):
        timeLeft = inter / self.MicroIntv
        while self.run_status == True & timeLeft > 0:
            time.Sleep(self.MicroIntv)
            timeLeft = timeLeft - 1
  
def main():
    t = TimeThread()
    t.start()

    while True:
        print "#--> type in 'exit' to exit"
        s = raw_input('#--> ')
        if 0 == cmp(s.lower(),"exit"):
            print "#--> Exit in at most [%d] secs..." % micro_interval
            t.stop()
            t.join()
            break
    

if __name__ == '__main__':
    main()
