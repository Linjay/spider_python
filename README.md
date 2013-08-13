spider_python
=============

抓取北邮人论坛和水木社区校招信息的爬虫程序, 直接运行main.py即可，非常简洁，可以扩展

程序依赖以下第三方Python包：requests, BeautifulSoup, redis-py
    
扩展自某大神https://github.com/lizherui/spider_python

不太会PHP，所以就直接用python导出html网页，挂载到TOMCAT下就OK
PYTHON脚本中会自动定时抓取，在main.py中可以设置相关参数，包括关键字，抓取间隔
在spider.py中可以设置所要抓取的网站，打开看看就知道改哪了

运行版本PYTHON 2.7.5（BS4在PY2.6.6以下的版本需要额外的扩展库，CENTOS用户需要注意了，我的解决方案是装了两个PYTHON，当然这个版本也可以在windows下运行，WIN7用户不用担心）

BeautifulSoup 4.2.1	http://www.crummy.com/software/BeautifulSoup/

Redis-py    https://github.com/andymccurdy/redis-py

requests	https://github.com/kennethreitz/requests

git clone到本地直接python setup install就OK