# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HereisclawerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SenicSpotItem(scrapy.Item):
    name = scrapy.Field()        # 名称
    lng = scrapy.Field()         # 经度
    lat = scrapy.Field()         # 纬度
    brief_intro = scrapy.Field() # 简介
    bg_img = scrapy.Field()      # 图片
    category = scrapy.Field()    # 类别(scenic)

    intro = scrapy.Field()       # 介绍
    warning = scrapy.Field()     # 提示
    image_urls = scrapy.Field()  # 用于ImagePipeline
    images = scrapy.Field()      # 用于ImagePipeline

class RestaurantItem(scrapy.Item):
    name = scrapy.Field()        # 名称
    lng = scrapy.Field()         # 经度
    lat = scrapy.Field()         # 纬度
    brief_intro = scrapy.Field() # 简介
    bg_img = scrapy.Field()      # 图片
    category = scrapy.Field()    # 类别(scenic)
    food_list = scrapy.Field()   # 菜谱
    image_urls = scrapy.Field()  # 用于ImagePipeline
    images = scrapy.Field()      # 用于ImagePipeline

