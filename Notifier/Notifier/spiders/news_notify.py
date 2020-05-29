import scrapy
import os
from pygame import mixer
import time
import notify2

class newsNotify(scrapy.Spider):

    notify2.init('News_Notifier')
    mixer.init()

    name = 'notify'
    start_urls = [
        'https://in.reuters.com/news/top-news'
    ]
    path = "/home/coder/Desktop/News_Notifier"

    def parse(self, response):
        title = response.xpath('//h3[@class="story-title"]/text()').extract()

        for item in title:
            item = str(item)
            item = item.translate(None,'\t\n')
            yield {'title' : item}
