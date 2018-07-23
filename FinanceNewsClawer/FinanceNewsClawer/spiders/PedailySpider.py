# -*- coding: utf-8 -*-

#################
# 投资界新闻爬虫 #
#################

import scrapy
from FinanceNewsClawer.items import NewsDetailItem
from w3lib.html import remove_tags, remove_comments, remove_tags_with_content

class PedailySpider(scrapy.Spider):
  name = "PedailySpider"

  custom_settings = {
    "LOG_LEVEL": "INFO", # log设置为INFO以减少控制台输出信息
    "ITEM_PIPELINES" : {
        'FinanceNewsClawer.pipelines.PedailySpiderPipeline' : 500
    },
    "RECORD_FILE": "FinanceNewsClawer/cfg/PerdailySpider.txt", # 保存爬取记录的文件
    "LOG_FILE": "log.log", # log文件
  }

  def start_requests(self):
    url = "http://www.pedaily.cn/first/"
    formdata = {
      "action": "post",
      "p": "1", # 页数
      "pagesize": "20", # 每页数量
      "url": "http://www.pedaily.cn/first/",
    }
    yield scrapy.FormRequest(url = url, callback = self.parse_list, formdata = formdata)
  
  def parse_list(self, response):
    # 上一次爬取的新闻网址
    with open(self.custom_settings["RECORD_FILE"], "r") as file:
      last_list = [ hash(x.strip()) for x in file.readlines() ]

    selector = scrapy.Selector(response=response)
    title_list = selector.xpath('//*[@id="firstnews-list"]/ul[position()>=1]/li/a/text()').extract()
    url_list = selector.xpath('//*[@id="firstnews-list"]/ul[position()>=1]/li/a/@href').extract()

    for url in url_list:
      if hash(url) in last_list:
        continue
      yield scrapy.Request(url = url, callback=self.parse)
    
    # 保存记录
    with open(self.custom_settings["RECORD_FILE"], "w") as file:
      file.write("\n".join(url_list))
  
  def parse(self, response):
    selector = scrapy.Selector(response=response)
    title = selector.xpath('//*[@id="newstitle"]/text()').extract_first()
    time = selector.xpath('//*[@id="final-content"]/div[1]/div/div[2]/div[1]/div[1]/span[1]/text()').extract_first()
    time += ":00"
    content = selector.xpath('//*[@id="news-content"]').extract_first()

    selector = scrapy.Selector(text=content)
    preview_image = selector.re_first('.*?<img.*?src="(.*?)"')

    yield NewsDetailItem(
      title = title,
      time = time,
      preview_image = preview_image,
      content = content
    )
