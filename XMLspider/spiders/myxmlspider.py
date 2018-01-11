# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/liuyuhaoxy.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}

        i['title'] = selector.select('/rss/channel/item/title/text()').extract()
        i['link'] = selector.select('/rss/channel/item/link/text()').extract()
        i['author'] = selector.select('/rss/channel/item/author/text()').extract()
        for j in range(len(i["title"])):
            print(i["title"][j])
            print(i["link"][j])
            print(i["author"][j])

        return i
