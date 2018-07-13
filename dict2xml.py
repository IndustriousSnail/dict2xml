# -*- coding: utf-8 -*-
from xml.dom.minidom import parseString

__author__ = 'snail'
__date__ = '2018/7/13'

attr_symbol = ('@', '-')
text_symbol = ('#text',)


def recursion(obj):
    """
    递归进行dict到xml转换
    :return: xml：一个节点内部xml, attrs：一个节点的属性
    """
    if not isinstance(obj, dict):
        raise RuntimeError("请传入dict对象")
    xml = ''
    attrs = []
    for key, value in obj.items():
        if len(key) > 0 and key[0:1] in attr_symbol:
            attrs.append(' ' + key[1:len(key)] + '=' + '"' + value + '"')
        elif key in text_symbol:
            xml = value
        else:
            child_attrs = []
            child_xml = ''
            is_list = False
            if isinstance(value, dict):
                # 子节点为dict
                child_xml, child_attrs = recursion(value)
            elif isinstance(value, list):
                # 子节点为list
                is_list = True
                for item in value:
                    # 遍历列表
                    if isinstance(item, dict):
                        child_xml, child_attrs = recursion(item)
                        xml += '<' + key
                        for child_attr in child_attrs:
                            xml += child_attr
                        xml += '>'
                        # add child
                        xml += child_xml
                        xml += '</' + key + '>'
                    else:
                        xml += '<' + key + '>' + item + '</' + key + '>'
            else:
                # 子节点为text
                child_xml = value
            if not is_list:
                # 如果不是列表则
                xml += '<' + key
                for child_attr in child_attrs:
                    xml += child_attr
                xml += '>'
                # add child
                xml += child_xml
                xml += '</' + key + '>'

    return xml, attrs


def dict2xml(obj):
    result = '<?xml version="1.0" encoding="utf-8"?>'
    result += recursion(obj)[0]  # 递归生成
    result = parseString(result).toprettyxml()
    return result

