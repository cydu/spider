# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class HomelinkItem(Item):
    # define the fields for your item here like:
    hid = Field()           #房屋id
    address = Field()       #地址(Eg: 海淀 铭科苑)
    house_style = Field()   #户型
    room_number = Field()   #房间数
    area = Field()          #面积
    date = Field()          #成交日期
    price = Field()         #成交价
    unit_price = Field()    #成交单价
    rise_rate = Field()     #升值幅度
    desc = Field()          #介绍
    contact = Field()       #联系人
    tag = Field()           #标签
    pass
