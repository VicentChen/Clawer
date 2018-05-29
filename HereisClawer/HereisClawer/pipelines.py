# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import threading

class HereisclawerPipeline(object):
    def process_item(self, item, spider):
        return item

class QunarSpiderPipeline(object):

    def __init__(self, mysql_conf):
        self.mysql_conf = mysql_conf
        self.spot_counter = 0; self.spot_lock = threading.Lock()
        self.scen_counter = 0; self.scen_lock = threading.Lock()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_conf = crawler.settings.get("MYSQL_CONF")
        )
    
    def open_spider(self, spider):
        try:
            self.conn = mysql.connector.connect(**self.mysql_conf)
            self.cursor = self.conn.cursor()
            spider.logger.info("MySQL连接成功")
        except TypeError as e:
            spider.logger.error("MySQL配置错误")
        except mysql.connector.Error as e:
            spider.logger.error("MySQL连接失败")
            spider.logger.error(e)
        
    def close_spider(self, spider):
        spider.logger.info("插入地点数据 %d 条" % self.spot_counter)
        spider.logger.info("插入景点数据 %d 条" % self.scen_counter)
        self.cursor.close()
        self.conn.close()
        spider.logger.info("关闭MySQL数据库")

    def process_item(self, item, spider):
        # 插入地点至数据库
        self.cursor.execute('''
            INSERT INTO spot
                (gps_lng, gps_lat, name, brief_intro, bg_img, category)
            VALUES
                (%f, %f, '%s', '%s', '%s', '%s');
        ''' % (
            item["lng"], item["lat"],
            item["name"], item["brief_intro"],
            item["bg_img"], item["category"]
        ))
        # 获取插入的地点ID
        spot_id = self.cursor.lastrowid
        self.conn.commit(); self.__inc_spot()

        # 插入景点至数据库
        self.cursor.execute('''
            INSERT INTO scenic_spot
                (spot_id, intro, warning)
            VALUES
                ('%s', '%s', '%s');
        ''' % (
            spot_id, item["intro"], item["warning"]
        ))
        self.conn.commit(); self.__inc_scen()
    
    def __inc_spot(self):
        with self.spot_lock:
            self.spot_counter += 1
    
    def __inc_scen(self):
        with self.scen_lock:
            self.scen_counter += 1