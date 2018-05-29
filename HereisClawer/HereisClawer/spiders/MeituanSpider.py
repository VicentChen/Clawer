# -*- coding: utf-8 -*-

##############
# 美团美食爬虫 #
##############

import scrapy
import json
import re
import time
import hashlib
from urllib.parse import urlencode
from HereisClawer.items import RestaurantItem

class MeituanSpider(scrapy.Spider):
    name = "MeituanSpider"

    custom_settings = {
        "REST_NUMBER" : "15", # 每次爬取条数，
        "UUID" : "unknown", # 美团分配的UUID，爬取过程中会自动获取
        "DOWNLOAD_DELAY": 1.5, # 下载速度控制
        "IMAGES_STORE" : "Product/MeituanSpider/images", # 图片保存路径
        "ITEM_PIPELINES" : {
            'scrapy.pipelines.images.ImagesPipeline': 1,
            'HereisClawer.pipelines.MeituanSpiderPipeline' : 500
        }
    }

    def start_requests(self):
        self.logger.info("开始预访问美团美食页面")
        url = "http://meishi.meituan.com/i/?ci=59&stid_b=1"
        yield scrapy.Request(url=url, callback=self.parse_preget)
    
    def parse_preget(self, response):
        self.logger.info("预访问完成")
        cookie_raw = response.headers.getlist('Set-Cookie') # 获取Cookie字符串
        for raw in cookie_raw:
            if str(raw, "utf-8").startswith('uuid'):
                self.custom_settings["UUID"] = re.match('uuid=(.*?);', str(raw, "utf-8")).group(1)
        self.logger.info("当前uuid为 %s " % self.custom_settings["UUID"] )

        # 查询列表
        query_data = {
            "uuid": self.custom_settings["UUID"],
            "version":"8.3.3",
            "platform":"3",
            "app":"",
            "partner":"126",
            "riskLevel":"1",
            "optimusCode":"10",
            "originUrl":"http://meishi.meituan.com/i/?ci=59&stid_b=1", # 此处应当与start_request中的url一致
            "offset":"0", # 偏移量，第一页为0，第二页为15，以此类推
            "limit":self.custom_settings["REST_NUMBER"], # 每一页的商家数目
            "cateId":"1", # 美食分类
            "lineId":"0",
            "stationId":"0",
            "areaId":"0",
            "sort":"default",
            "deal_attr_23":"",
            "deal_attr_24":"",
            "deal_attr_25":"",
            "poi_attr_20043":"",
            "poi_attr_20033":""
        }
        self.logger.info("开始获取餐厅列表")
        url = 'http://meishi.meituan.com/i/api/channel/deal/list'
        yield scrapy.FormRequest(url=url, formdata=query_data, callback=self.parse)

    def parse(self, resposne):
        # 获取餐厅列表对象
        try:
            rest_list = json.loads(resposne.text)["data"]["poiList"]["poiInfos"]
            self.logger.info("餐厅列表获取完成")
            self.logger.info("获取餐厅数据 %d 条" % len(rest_list))
        except BaseException as e:
            self.logger.error(e)
            self.logger.error("餐厅列表获取失败")
            return
        
        # 菜谱初始URL
        deallist_url = 'http://meishi.meituan.com/i/api/poi/deallist'
        # 菜谱查询初始数据
        query_data = {
            "uuid":self.custom_settings["UUID"],
            "version":"8.3.3",
            "platform":"3",
            "app":"",
            "partner":"126",
            "riskLevel":"1",
            "optimusCode":"10",
            "originUrl": "TO_FILL",
            "poiId": "TO_FILL"
        }

        self.logger.info("开始访问商家菜单")
        for rest in rest_list:
            rest_obj = {
                "餐厅名": rest["name"],
                "经度": rest["lng"],
                "纬度": rest["lat"],
                "图片": rest["frontImg"],
            }
            
            poiid = rest["poiid"] # 地点ID
            ctpoi = rest["ctPoi"] # 未知参数，但请求时需要使用
            # 商家主页URL
            origin_url = "http://meishi.meituan.com/i/poi" + "/" + poiid + "?ct_poi=" + ctpoi
            # 组建查询数据
            query_data["originUrl"] = origin_url
            query_data["poiId"] = poiid

            yield scrapy.FormRequest(url=deallist_url, formdata=query_data, meta=rest_obj, callback=self.parse_deallist)
    
    def parse_deallist(self, response):
        rest_obj = response.meta
        food_list = json.loads(response.text)["data"]["dealArr"]
        food_list_obj = [
            {
                "名称": food["title"],
                "价格": food["price"],
                "图片": "http:" + food["imgUrl"],
                "类别": "default",
            }
            for food in food_list
        ]
        rest_obj["菜谱"] = food_list_obj
        
        # 构建待下载图片列表
        auto_add_scheme = lambda x : "http:" + x if x.startswith("//") else x
        img_list = [ auto_add_scheme(food["图片"]) for food in food_list_obj ]
        img_list.append(auto_add_scheme(rest_obj["图片"]))

        # 更正图片名称
        rest_obj["图片"] = time.strftime("%Y/%m/%d/") + hashlib.sha1(rest_obj["图片"].encode("utf-8")).hexdigest() + ".jpg"
        for food in food_list_obj:
            food["图片"] = time.strftime("%Y/%m/%d/") + hashlib.sha1(food["图片"].encode("utf-8")).hexdigest() + ".jpg"

        yield RestaurantItem(
            name = rest_obj["餐厅名"], category = "restaurant",
            lng = rest_obj["经度"], lat = rest_obj["纬度"],
            brief_intro = rest_obj["餐厅名"], # TODO: 餐厅介绍
            bg_img = rest_obj["图片"],
            food_list = rest_obj["菜谱"],
            image_urls = img_list
        )
