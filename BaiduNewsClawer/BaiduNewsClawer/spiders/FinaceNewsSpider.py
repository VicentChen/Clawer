# -*- coding: utf-8 -*-

###################
# 百度财经新闻爬虫 #
###################

import scrapy
import time
from BaiduNewsClawer.items import NewsItem

class FinaceNewsSpider(scrapy.Spider):
  name = "FinaceNewsSpider"

  custom_settings = {
    "LOG_LEVEL": "INFO", # log设置为INFO以减少控制台输出信息
    "ITEM_PIPELINES" : {
        'BaiduNewsClawer.pipelines.BaidunewsclawerPipeline' : 500
    },
    "RECORD_FILE": "BaiduNewsClawer/cfg/last.txt", # 保存爬取记录的文件
    "LOG_FILE": "log.log", # log文件
  }

  start_urls = [
    "http://news.baidu.com/finance"
  ]

  def start_requests(self):
    for url in self.start_urls:
      yield scrapy.Request(url=url, callback=self.parse_list)
  
  def parse_list(self, response):
    # 上一次爬取的新闻网址
    with open(self.custom_settings["RECORD_FILE"], "r") as file:
      last_list = [ hash(x.strip()) for x in file.readlines() ]

    selector = scrapy.Selector(response=response)

    url_list = []
    title_list = []

    # 财经头条
    headline_url_list = selector.xpath('//*[@id="col_focus"]/div[2]/div/ul[position()>=1]/li[position()>=1]/a/@href').extract()
    headline_title_list = selector.xpath('//*[@id="col_focus"]/div[2]/div/ul[position()>=1]/li[position()>=1]/a/text()').extract()
    self.logger.info("解析财经头条 %d 条" % len(headline_url_list))
    url_list += headline_url_list
    title_list += headline_title_list

    for (title, url) in zip(title_list, url_list):
      # 判断是否已添加至数据库
      if hash(url) in last_list:
        continue

      yield NewsItem(
        title = title,
        url = url,
        time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
      )

    # 保存记录
    with open(self.custom_settings["RECORD_FILE"], "w") as file:
      file.write("\n".join(url_list))
