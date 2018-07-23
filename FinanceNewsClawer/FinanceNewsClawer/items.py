# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancenewsclawerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsDetailItem(scrapy.Item):
    title = scrapy.Field()
    preview_image = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
