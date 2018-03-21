# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'

import scrapy
from scrapy import Selector


class JackSpider(scrapy.Spider):
    name = "Jack"
    start_urls = ['https://www.torrentkitty.tv/search/蜜桃',]

    def parse(self, response):
        yield{
            'name': response.xpath('//td[re:test(@class,"name")]//@text').extract(),
            'url': response.xpath('//a[re:test(@href,"magnet*")]//@href').extract(),
        }

# scrapy runspider TorrentKitty.py -o res.json