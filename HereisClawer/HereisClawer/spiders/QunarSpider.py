# -*- coding: utf-8 -*-

###################
# 去哪儿热门景点爬虫 #
###################

import scrapy
import json

class QunarSpider(scrapy.Spider):
    name = "QunarSpider"

    custom_settings = {
        "LOG_LEVEL": "INFO", # log设置为INFO以减少控制台输出信息
        "TOTAL_PAGES" : 100, # 爬取页数
    }

    def start_requests(self):
        # URL模板，指向去哪儿景点搜索页
        url_template = r"http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&sort=pp&page="
        urls = [url_template + str(i+1) for i in range(self.custom_settings["TOTAL_PAGES"])]
        self.logger.info("构建URL %d 条" % len(urls))

        for i, url in enumerate(urls):
            yield scrapy.Request(url=url, callback=self.parse_list, meta={"index" : i+1})
    
    def parse_list(self, response):
        index = response.meta["index"] # 获取当前页数
        self.logger.info("热门景点第 %d 页爬取完成" % index)
        self.logger.info("开始提取第 %d 页热门景点信息" % index)

        selector = scrapy.Selector(response=response) # 构建选择器
        # 获取经纬度，名称，URL，背景图片
        spot_gps = selector.xpath('//*[@id="search-list"]/div[position()>=1]/@data-point').extract()
        spot_names = selector.xpath('//*[@id="search-list"]/div[position()>=1]/div/div[2]/h3/a/text()').extract()
        spot_urls  = selector.xpath('//*[@id="search-list"]/div[position()>=1]/div/div[2]/h3/a/@href').extract()
        spot_bgs = selector.xpath('//*[@id="search-list"]/div[position()>=1]/div/div[1]/div/a/img/@data-original').extract()
        # 构建景点
        spots = [
            {
                "名称": spot_names[i],
                "经度": float(spot_gps[i].split(",")[0]),
                "纬度": float(spot_gps[i].split(",")[1]),
                "背景": spot_bgs[i],
            }
            for i in range(len(spot_gps))
        ]
        self.logger.info("解析景点信息 %d 条" % len(spots))
        # 访问景点URL
        for i, url in enumerate(spot_urls):
            yield scrapy.Request(url="http://piao.qunar.com" + url, callback=self.parse, meta={"spot" : spots[i]})
    
    def parse(self, response):
        spot = response.meta["spot"] # 获取部分构建的景点

        selector = scrapy.Selector(response=response) # 构建选择器
        # 获取简介，介绍，景点图片
        brief_intro = selector.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/text()').extract_first()
        intro = selector.xpath('//*[@id="mp-charact"]/div[1]/div[1]/div[1]/p/text()').extract_first()
        imgs = selector.xpath('//*[@id="mp-charact"]/div[2]/div[1]/div/img/@src').extract() 
        spot["简介"] = brief_intro; spot["介绍"] = intro; spot["图片"] = imgs
        
        with open("Product/QunarSpider/spots.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(spot, ensure_ascii=False) + ",\n")
