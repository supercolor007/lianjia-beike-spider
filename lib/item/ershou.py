#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, name, total_price, unit_price, desc, url):
        self.district = district
        self.area = area
        self.total_price = total_price
        self.unit_price = unit_price
        self.name = name
        self.desc = desc
        self.url = url

    def text(self):
        return self.district + "," + \
               self.area + "," + \
               self.name + "," + \
               self.total_price + "," + \
               self.unit_price + "," + \
               self.desc + "," + \
               self.url
