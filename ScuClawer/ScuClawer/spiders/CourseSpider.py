# -*- coding: utf-8 -*-

##########################
# 川大教务系统课程列表爬虫 #
##########################

import scrapy

class CourseSpider(scrapy.Spider):
    name = "CourseSpider"

    custom_settings = {
        "TERM_CODE": "2017-2018-2-1", # 学期号
        "TOTAL_COURSES": "5436", # 要获取的课程数，建议人工填写
    }

    def start_requests(self):
        url = "http://zhjw.scu.edu.cn/loginAction.do" # 登陆页
        data = {
            # 个人信息
            "zjh": 请输入账号(字符串类型), # 账号
            "mm": 请输入密码(字符串类型) # 密码
        }
        self.logger.info("开始登陆教务处")
        self.logger.info("账号: %s 密码: %s" % (data["zjh"], data["mm"]))
        yield scrapy.FormRequest(url = url, formdata = data, callback = self.pre_get)

    # 预访问
    def pre_get(self, response):
        self.logger.info("教务处登陆")
        url = "http://zhjw.scu.edu.cn/kckbcxAction.do?oper=kckb_lb"
        self.logger.info("开始预访问教室查询页")
        yield scrapy.Request(url = url, callback = self.get_courses, dont_filter = True)

    # 获取课程列表
    def get_courses(self, response):
        self.logger.info("教室查询页访问成功")
        url = "http://zhjw.scu.edu.cn/kckbcxAction.do?oper=kbtjcx"
        data = {
            "kcxnxq": self.custom_settings["TERM_CODE"], 
            "kckcm": "",
            "xsh": "",
            "kckch": "",
            "kckxh": "",
            "pageSize": self.custom_settings["TOTAL_COURSES"], 
            "page": "1",
            "currentPage": "1",
            "pageNo": "",
        }
        self.logger.info("开始查询 %s 学年课程，查询数量为 %s 条" % (self.custom_settings["TERM_CODE"], self.custom_settings["TOTAL_COURSES"]))
        yield scrapy.FormRequest.from_response(response = response, url = url, formname="kckbForm", formdata = data, callback = self.parse)

    # 页面解析
    def parse(self, response):
        self.logger.info("查询成功")
        selector = scrapy.Selector(response=response)
        headers = selector.xpath('//*[@id="user"]/thead/tr/th[position() >= 2 and position() <= 8]/text()').extract()
        infos = selector.xpath('//*[@id="user"]/tbody/tr[position() >= 1]/td[position() >= 2 and position() <= 8]/text()').extract()

        i = 0; length = len(infos)
        courses = []
        while i < length:
            course = {}
            for header in headers:
                course[header] = infos[i].strip()
                i = i + 1
            courses.append(course)
        self.logger.info("解析课程信息 %d 条" % len(courses))
