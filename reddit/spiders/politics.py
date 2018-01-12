# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import NewsItem
import time

class PoliticsSpider(CrawlSpider):
    name = "reddit_politics"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['https://www.reddit.com/r/politics/']

    rules = [
        Rule(LinkExtractor(
        	allow=['/r/politics/\?count=\d*&after=\w*']),
        	callback='parse_item',
        	follow=True),
    ]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = NewsItem()
            item['type'] = 'Politics'
            item['title'] = selector.xpath('div/p/a/text()').extract()
            item['url'] = selector.xpath('a/@href').extract()
            item['timeretrieved'] = time.strftime("%d/%m/%Y-%H:%M:%S")

            yield item
