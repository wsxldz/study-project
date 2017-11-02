# -*- coding: utf-8 -*-

# Scrapy settings for Cboss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Cboss'

SPIDER_MODULES = ['Cboss.spiders']
NEWSPIDER_MODULE = 'Cboss.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Cboss (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 50

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
    'Accept-Encoding' : 'gzip, deflate, br' ,
    'Accept-Language' : 'zh-CN,zh;q=0.8' ,
    'Cache-Control' : 'no-cache' ,
    'Connection' : 'keep-alive' ,
    'Cookie' : 'user_trace_token=20171012164449-215f45ee-9761-480f-84c5-cbb9e626ffda; LGUID=20171012164457-a08515cf-af29-11e7-8f69-525400f775ce; X_HTTP_TOKEN=f1137919f22dc2bf1fd6e7b5147d617f; X_MIDDLE_TOKEN=5f03528107cd73966c7ac146c4278daa; TG-TRACK-CODE=index_navigation; SEARCH_ID=d7619f3f4f68480e8cba21040ef26fb7; JSESSIONID=ABAAABAAADEAAFI2ABB7D3B1FA22592D261AE2FCA6A2E19; _gat=1; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60yUKm0FNkUsKqsSdu00000PW4pNb00000XRRNRM.THL0oUhY1x60UWdBmy-bIfK15yfkmWPbmWm3nj0snHn3nhD0IHYsrDcLwRFanjuArjn4fYDvwDujnWwKnHmYnjfYwb77rfK95gTqFhdWpyfqn101n1csPHnsPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5Hn3rjb1%26tpl%3Dtpl_10085_15730_11224%26l%3D1500117464%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m6c247d9c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D220%26ie%3Dutf-8%26f%3D3%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3Dscrapy%252520%2525E5%252587%2525BA%2525E7%25258E%2525B0%2525E9%252587%25258D%2525E5%2525AE%25259A%2525E5%252590%252591%26rqlang%3Dcn%26inputT%3D4003%26prefixsug%3D%2525E6%25258B%252589%2525E9%252592%2525A9%26rsp%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _putrc=E0BE960D39366DEE; login=true; unick=%E5%90%B4%E5%B3%BB%E6%9D%B0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E6%9D%AD%E5%B7%9E; _gid=GA1.2.143482011.1508643461; _ga=GA1.2.1884262362.1507797792; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508646653,1508721676,1508727426,1508754187; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508754213; LGSID=20171023182507-71015cb7-b7dc-11e7-960c-5254005c3644; LGRID=20171023182532-7fe26ef2-b7dc-11e7-a576-525400f775ce' ,
    'Host' : 'www.lagou.com' ,
    'Pragma' : 'no-cache' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' ,
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Cboss.middlewares.CbossSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Cboss.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Cboss.pipelines.CbossPipeline': 1,
   'scrapy_redis.pipelines.RedisPipeline':999,#数据统一存到redis服务器上 管道文件
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#---------------------------------------------------------------------------
#url过滤 用scrapy_redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#调度器改成scrapy_redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#可以暂停
SCHEDULER_PERSIST = True

#队列改成scrapy_redis
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" #优先级
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"  # 栈  先进后出

#redis服务器的 ip地址和端口号
REDIS_HOST = '192.168.2.212'
REDIS_PORT = 6379

# CONCURRENT_ITEMS = 100
# CONCURRENT_REQUEST = 99 #并发
# CONCURRENT_REQUEST_PER_DOMAIN = 99 #并发最大限制

