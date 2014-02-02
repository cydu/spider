# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from homelink.items import HomelinkItem

class LinkHomeSpider(Spider):
    name = "homelink"
    url_prefix = "http://beijing.homelink.com.cn/"
    allowed_domains = ["beijing.homelink.com.cn"]
    start_urls = [
        "http://beijing.homelink.com.cn/sold/c1111027378318/rs铭科苑/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        sel = Selector(response)
        houses = sel.xpath('//div[@id="listData"]//div[@class="public indetail"]')
        for house in houses:
            item = HomelinkItem()
            #style = house.xpath('@style').extract()[0]
            item['hid'] = house.xpath('h3//a/@href').re(u'/sold/(.*).shtml')[0]
            item['title'] = "".join(house.xpath('h3//text()').extract())
            item['date'] = house.xpath('div[@class="price"]/ul/text()').extract()[0]
            item['price'] = "".join(house.xpath('div[@class="priceo"]/ul/span/text()').extract() + house.xpath('div[@class="priceo"]/ul/label/text()').extract())
            item['unit_price'] = "".join(house.xpath('div[@class="priceoo"]/ul/span/text()').extract() + house.xpath('div[@class="priceoo"]/ul/label/text()').extract())
            item['rise_rate'] = house.xpath('div[@class="priceooo"]/ul/text()').extract()[0]
            item['desc'] = "".join(house.xpath('div[@class="content"]/p[@class="clearfix"]/text()').extract())
            item['contact'] = house.xpath('div[@class="content"]/p[@class="clearfix"]/a/@href').extract()[0]
            item['tag'] = ",".join(house.xpath('div[@class="content"]/ol/label/text()').extract())
            yield item
            #print hid, title, date, price, unit_price, rise_rate, desc, contact, tag
            
        for url in sel.xpath('//div[@class="fanye"]/ul/a/@href').extract():
            yield Request(self.url_prefix + url, callback=self.parse)

