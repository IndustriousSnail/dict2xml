# dict2xml
将dict转为xml
Convert python dict to xml

由于项目需要，但是没有从github中找到合适的，所以就自己写了一个。

暂时只支持简单的dict到xml的转换。

例如：
```
{
  "root": {
    "child": {
      "-name": "test",
      "list": [
        {
          "-name": "list1",
          "#text": "list1-content"
        },
        {
          "-name": "list2",
          "#text": "list2-content"
        },
        {
          "-name": "list3",
          "#text": "list3-content"
        }
      ]
    }
  }
}
```
 转为xml则为
```
<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <child name="test">
    <list name="list1">list1-content</list>
    <list name="list2">list2-content</list>
    <list name="list3">list3-content</list>
  </child>
</root>
```
xml转为json的规则是按照 https://www.bejson.com/xml2json/ 该网址来的。

