# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import threading

class FinancenewsclawerPipeline(object):
    def process_item(self, item, spider):
        return item

class PedailySpiderPipeline(object):
    def __init__(self, mysql_conf):
        self.mysql_conf = mysql_conf
        self.news_detail_counter = 0; self.news_detail_lock = threading.Lock()

    @classmethod
    def from_crawler(cls, crawler):
        mode = crawler.settings.get("MODE")
        if mode == "DEPLOY":
            return cls(
                mysql_conf = crawler.settings.get("STB_MYSQL_CONF")
            )
        else:
            return cls(
                mysql_conf = crawler.settings.get("DEV_MYSQL_CONF")
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
        spider.logger.info("插入新闻 %d 条" % self.news_detail_counter)
        self.cursor.close()
        self.conn.close()
        spider.logger.info("关闭MySQL数据库")

    def process_item(self, item, spider):
        # 插入新闻至数据库
        self.cursor.execute('''
            INSERT INTO news_detail
                (title, preview_image, time, content)
            VALUES
                (%s, %s, %s, %s);
        ''', (
            item["title"], item["preview_image"], item["time"], item["content"]
        ))
        self.conn.commit(); self.__inc_news();
    
    def __inc_news(self):
        with self.news_detail_lock:
            self.news_detail_counter += 1