spider_python
=============

抓取北邮人论坛和水木社区校招信息的爬虫程序, 非常简洁，可以扩展。

爬虫根据自定义关键字先对校招信息进行过滤，然后存储到本机redis中。本机若有lamp环境，可直接从redis读取信息到web页面上即可，lamp环境中的php程序示例如下：

    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to spider!</title>
    <style>
        body {
            width: 35em;
            margin: 0 auto;
        }
        a:visited { color: red; }
    </style>
    </head>
    <body>
    <?php
    $rs_ip = '127.0.0.1';
    $rs_port = 6379;
    $rs = new Redis();
    $rs->connect($rs_ip, $rs_port);
    $ret = $rs->smembers('urls');
    foreach($ret as $herf) {
        echo $herf . "<br/>";
    }
    ?>
    </body>
    </html>

效果截图：
    
![1](https://lh3.googleusercontent.com/-mqsrIBbWj4A/UfiLMw4sW2I/AAAAAAAAAGE/_IHC__pJVxE/w958-h190-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-07-31+%25E4%25B8%258A%25E5%258D%258811.56.48.png)

Enjoy it。

