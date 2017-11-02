# -*- coding: utf-8 -*-
from Cboss.items import CbossItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import scrapy




class BossSpider(RedisCrawlSpider):
    name = 'boss'
    allowed_domains = ['lagou.com']
    # start_urls = ['https://www.lagou.com/']
    redis_key = 'lagou:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'jobs/list_?.*'),follow=True),
        Rule(LinkExtractor(allow=r'zhaopin/.*'),follow=True,callback='detail_parse'),
        #Rule(LinkExtractor(allow=r'jobs/\d+.html'),callback='parse_item',follow=True),
    )

    def detail_parse(self,response):
        #print response.url
        detail_url_list = response.xpath('//a[@class="position_link"]/@href').extract()
        for detail_url in detail_url_list:
            yield scrapy.Request(detail_url,callback=self.parse_item,priority=1)
        #yield scrapy.Request(url,)

    def parse_item(self, response):
        print 123
        print response.url
        item = CbossItem()
        url = response.url
        item['url'] = url
        item['position'] = response.xpath('//div[@class="position-content-l"]//span[@class="name"]/text()').extract()[0].strip()
        item['company'] = response.xpath('//dl[@class="job_company"]//h2/text()[1]').extract()[0].strip()
        item['location'] = response.xpath('//div[@class="work_addr"]/text()[4]').extract()[0].strip()
        item['time'] = response.xpath('//p[@class="publish_time"]/text()').extract()[0].strip()
        duty_list = response.xpath('//dd[@class="job_bt"]').extract()
        for dut in duty_list:
            duty = dut.strip()
            item['duty'] = duty
        item['salary'] = response.xpath('//div[@class="position-content-l"]//p/span[1]/text()').extract()[0].strip()
        yield item
