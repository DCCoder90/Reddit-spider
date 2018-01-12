# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import NewsItem
import time


class WorldSpider(CrawlSpider):
    name = "reddit_general"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['https://www.reddit.com/r/news/']
    rules = [
        Rule(LinkExtractor(
        	allow=['/r/news/\?count=\d*&after=\w*']),
        	callback='parse_item',
        	follow=True),
    ]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = NewsItem()
            item['type'] = 'General'
            item['title'] = selector.xpath('div[2]/p[1]/a[1]/text()').extract()
            item['url'] = selector.xpath('div[2]/p[1]/a[1]/@href').extract()
            item['timeretrieved'] = time.strftime("%d/%m/%Y-%H:%M:%S")

            yield item
