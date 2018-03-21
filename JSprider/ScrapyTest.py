# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'

import scrapy

class JackSpider(scrapy.Spider):
    name = "Jack"
    start_urls = ['https://morvanzhou.github.io/',]

    def parse(self, response):
        yield{
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace("",""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url, callback=self.parse)