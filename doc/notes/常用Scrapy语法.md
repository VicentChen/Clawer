# 常用Scrapy语法

## Request & Response

 - GET: `yield scrapy.Request(url=url, meta=dict, callback=self.callback)`
  - dict表示传递至`callback`的参数
 - POST: `yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.callback)`

## 持久化
 - JSON文件保存 `file.write(json.dumps(json_obj, ensure_ascii=False))`