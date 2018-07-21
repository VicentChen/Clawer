# Clawer

## Learn
 - `gramma.py` - Python基本语法
 - `scrapy/` - scrapy基本用法

## ScuClawer - 基于Scrapy框架的川大网站爬虫
 - 使用方法：进入`ScuClawer`目录下`scrapy crawl spidername`，"spidername"为下列爬虫名字

 ### **CirSpider - 教室信息发布系统爬虫**
 - 网页地址: http://202.115.47.164/cir/index.html
 - 获取数据: 当天所有教室占用信息
 - 格式: JSON
 - 示例: `ScuClawer/Product/CirSpider`
    - `classrooms.json`: 所有教室
    - `courses.json`: 所有课程,(此文件经过手动修改以适应JSON格式)

 ### **CourseSpider - 课程列表爬虫**
- 网页地址: http://zhjw.scu.edu.cn/kckbcxAction.do?oper=kbtjcx
 - 获取数据: 指定学年的所有课程信息
 - 格式: python-list
 - 示例: `ScuCLawer/Product/CourseSpider`
    - `courses.html`: 2017-2018学年春季学期所有课程
    - `courses.json`: 2017-2018学年春季学期所有课程前20条信息
    - `courses-complete.json` : 2017-2018学年春季学期所有课程信息，包括上课时间，上课地点等
    - `FailPages/`: 包含常见解析错误示例页面

 #### **注意事项**
  - `settings.py`中必须设置User-Agent才能够正常访问
  - 必须首先进行GET请求教室查询网页，然后才能够成功POST访问，否则会返回`500 Internal Server Error`，具体错误为`NullPointerException`，可能与教务处网页中的`history`有关
  - 查询时间可能稍长，log中未报错即为正常运行

## HereisClawer - [Hereis][2]信息爬虫
 隶属于项目[Hereis][2]的信息爬虫

 ### QunarSpider - 去哪儿热门景点爬虫
 - 网页地址: http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&sort=pp&page=1
 - 获取数据: 景点GPS，简介，介绍，图片等
 - 格式: JSON
 - 示例:
   - `HereisClawer/Product/QunarSpider/spot.json`
   - `HereisClawer/Product/QunarSpider/spot.jpg`
  - 注意事项: 爬取时**注意控制速度**，否则容易被封IP

 ### MeituanSpider - 美团附近美食爬虫
  - 网页地址(手机版): https://meishi.meituan.com/i/?ci=59&stid_b=1
  - 获取数据: 附近餐厅名称，GPS，团购菜单等
  - 格式: JSON
  - 示例: `HereisClawer/Product/MeituanSpider/`

## Utils - 爬虫辅助工具

### **`simple-deskewing`**
 - 简单的图像旋转矫正，适用于白底黑字不粘连/重合的验证码
 - 原理: 计算图片每一列黑色像素值，非0部分即为文字，进而分割图片为若干部分；为每一部分计算图片中文字的包围盒及其倾斜角度，最后旋转图片并拼接
 - 作用: 旋转后提升tesseract识别率
 - 示例: 
  <figure>
      <img src="doc/img/origin.jpg">
      <img src="doc/img/deskewing.jpg">
  </figure> 

### 分页爬取
分页爬取通过配置起始页、爬取页数实现，配置位置为`custom_settings`
 - 起始页: `START_PAGE`
 - 总页数: `TOTAL_PAGE`

## 环境与工具
 - **Python 3**
 - VSCode

 [1]: doc/img/origin
 [2]: https://github.com/CicadaTalk/hereis