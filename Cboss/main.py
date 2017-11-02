from scrapy import cmdline
#cmdline.execute('scrapy crawl boss'.split())


import os
os.chdir('spiders')
cmdline.execute('scrapy runspider boss.py'.split())







