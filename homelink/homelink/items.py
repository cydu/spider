# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class HomelinkItem(Item):
    # define the fields for your item here like:
    hid = Field()           #房屋id
    title = Field()         #标题
    date = Field()          #成交日期
    price = Field()         #成交价
    unit_price = Field()    #成交单价
    rise_rate = Field()     #升值幅度
    desc = Field()          #介绍
    contact = Field()       #联系人
    tag = Field()           #标签
    pass
