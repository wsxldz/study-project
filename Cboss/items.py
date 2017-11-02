# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CbossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名
    position = scrapy.Field()
    #公司名
    company = scrapy.Field()
    #工作地点
    location = scrapy.Field()
    #发布时间
    time = scrapy.Field()
    #岗位职责
    duty = scrapy.Field()
    #薪资
    salary = scrapy.Field()
    #url
    url = scrapy.Field()

