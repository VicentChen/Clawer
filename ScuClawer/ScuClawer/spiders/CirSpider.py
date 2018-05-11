# -*- coding: utf-8 -*-

#####################
# 教室信息发布系统爬虫 #
#####################

import scrapy
import json
import logging

class CirSpider(scrapy.Spider):
    name = "CirSpider"

    start_urls = [
        "http://202.115.47.164/cir/jxlConfig"
    ]

    def start_requests(self):
        for url in self.start_urls:
            self.logger.info("开始获取 %s" % (url))
            yield scrapy.FormRequest(url=url, formdata = "", callback = self.parse_classroom)

    def parse_classroom(self, response):
        building_list = json.loads(response.text)
        self.logger.info("获取教学楼信息 %d 条" % (len(building_list)))

        course_query_url = "http://202.115.47.164/cir/XLRoomData"
        for building in building_list:
            formdata = { "jxlname" : building["location"] }
            self.logger.info("开始获取教学楼 %s 课程信息" % (building["name"]))
            yield scrapy.FormRequest(url = course_query_url, formdata = formdata, callback = self.parse_course)

    def parse_course(self, response):
        course_list = json.loads(response.text)["roomdata"]
        self.logger.info("获取课程信息 %d 条" % (len(course_list)))
        # TODO: 处理已收集数据
