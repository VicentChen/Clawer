# -*- coding: utf-8 -*-

##########################
# 川大教务系统课程列表爬虫 #
##########################

import scrapy
from urllib.parse import urlencode
import json
import re
import logging

class CourseSpider(scrapy.Spider):
    name = "CourseSpider"

    custom_settings = {
        "LOG_LEVEL": "INFO", # log设置为INFO以减少控制台输出信息
        "TERM_CODE": "2017-2018-2-1", # 学期号
        "TOTAL_COURSES": "1", # 要获取的课程数，建议人工填写
        # "SPIDER_MIDDLEWARES": { # 此处为自定义的爬虫中间件，可用于DEBUG
        #     "ScuClawer.middlewares.CourseSpiderErrorSavingMiddleware": 1000, # 错误处理
        # }
    }

    def start_requests(self):
        self.logger.setLevel(logging.INFO)
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
        self.logger.info("教务处登陆成功")
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
        # header可自定义，但header顺序应为：课程号，课程名，课序号，学分，考试类型，系所，教师
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

        self.logger.info("开始解析课程课表")
        params = {
            "oper": "kckb_xx", # 操作为课程课表查询
            "xzxjxjhh": self.custom_settings["TERM_CODE"], # 学年号
            "xkch": "", # 课程号
            "xkxh": "", # 课序号
            "xjclxdm": "01", # ??未知，但所有请求均为01
            "xkcm": "", # 课程名，可不填
            "xxnxqm": "", # ??，可不填
            "xzxjxjhm": "", # ??，可不填
            "kclist": "", # ??，可不填
        }
        for course in courses:
            params["xkch"] = course[headers[0]] # header[0]为课程号
            params["xkxh"] = course[headers[2]] # header[2]为课序号
            time_url = "http://zhjw.scu.edu.cn/kcKbInfoAction.do?" + urlencode(params) # 课表查询URL
            yield scrapy.Request(url=time_url, callback=self.parse_time, meta={"course": course, "headers": headers})
        self.logger.info("课程课表解析结束")

    # 课表解析
    def parse_time(self, response):
        course = response.meta["course"] # 接收传来的meta
        selector = scrapy.Selector(response=response)
        table = selector.xpath('//*[@id="user"]/thead/tr[position() >= 2]/td[position() >= 2]/text()').extract()
        for i, item in enumerate(table):
            table[i] = item.strip()
        # 删除字符串 “第一节” “第五节” “第十节”
        del table[0]; del table[28]; del table[63]

        # 计算上课时间
        day_table = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        class_table = ["第一节", "第二节", "第三节", "第四节", "第五节", "第六节", "第七节", "第八节", "第九节", "第十节", "第十一节", "第十二节", "第十三节"]
        course_time = []
        for i, item in enumerate(table):
            if item: # item不为空
                # 正则表达式可保证即使出现多余括号亦能正常解析，re.S为多行匹配模式
                infos = re.match(r".*?\((..),(.*?),(.*?),(.*?),(.*?)\)", item, re.S).groups()

                day_no = i % 7 # 周 x
                class_no = i // 7 # 第 x 节
                course_time.append({
                    "周次" : infos[4],
                    "上课时间" : day_table[day_no] + class_table[class_no],
                    "上课地点" : infos[0] + "校区" + infos[1] + infos[2],
                    "授课教师" : infos[3],
                })
        course["课表"] = course_time
