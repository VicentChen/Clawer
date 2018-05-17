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

## 环境与工具
 - **Python 3**
 - VSCode