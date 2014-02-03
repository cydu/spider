# -*- coding: utf-8 -*-
import random
import urllib
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.project import get_project_settings as Settings
from captcha import Captcha
from homelink.items import HomelinkItem

class LoginSpider(CrawlSpider):
    name = 'login'
    allowed_domains = [Settings().get('HOMELINK_DOMAIN')]
    start_urls = [Settings().get('HOMELINK_LOGIN_URL')]

    rules = [
        Rule(SgmlLinkExtractor(), follow=True)
    ]

    def __init__(self):
        self.c = Captcha()
        self.c.loadData("./iconset/")
        self.is_login = False

    def parse(self, response):
        if self.is_login:
            return Request(Settings().get('HOMELINK_START_URL'), callback=self.parse_item)
        else:
            return self.login()

    def login(self):
        rid = (str)(random.random())
        url = "http://beijing.homelink.com.cn/validreg.php?" + rid
        urllib.urlretrieve(url, "/tmp/" + rid + ".jpg")

        validateCode = self.c.crack("/tmp/" + rid + ".jpg")
        yield FormRequest(url="http://beijing.homelink.com.cn/webregister/login.php?"+(str)(random.random()),
                    formdata={'username': Settings().get('HOMELINK_USERNAME'), 
                              'password': Settings().get('HOMELINK_PASSWORD'),
                              'validateCode': validateCode, 
                              'remember': '1', 
                              'dologin': '%E7%99%BB%E5%BD%95'}, 
                    callback=self.after_login)

    def after_login(self, response):
        # check login succeed before going on
        if response.status == 200 and response.url == "http://beijing.homelink.com.cn/center/":
            self.is_login = True
            return Request(Settings().get('HOMELINK_START_URL'), callback=self.parse_item)
        else:
            print "login Failed, try again. ", response.status, response.url
            return self.login()
    
    def parse_item(self, response):
        filename = response.url.split("/")[-2]
        sel = Selector(response)
        houses = sel.xpath('//div[@id="listData"]//div[@class="public indetail"]')
        for house in houses:
            item = HomelinkItem()
            #style = house.xpath('@style').extract()[0]
            item['hid'] = house.xpath('h3//a/@href').re(u'/sold/(.*).shtml')[0]
            title = ("".join(house.xpath('h3//text()').extract())).split(' ')
            item['address'] = " ".join(title[0:2])
            item['house_style'] = title[2]
            item['room_number'] = int(filter(lambda x:x.isdigit(),title[2]))
            item['area'] = int(filter(lambda x:x.isdigit(),title[3]))
            item['date'] = house.xpath('div[@class="price"]/ul/text()').extract()[0]
            item['price'] = "".join(house.xpath('div[@class="priceo"]/ul/span/text()').extract() + house.xpath('div[@class="priceo"]/ul/label/text()').extract())
            if item['price']:
                item['price'] = int(filter(lambda x:x.isdigit(), item['price'])) 
            item['unit_price'] = "".join(house.xpath('div[@class="priceoo"]/ul/span/text()').extract() + house.xpath('div[@class="priceoo"]/ul/label/text()').extract())
            if item['unit_price']:
                item['unit_price'] = int(filter(lambda x:x.isdigit(), item['unit_price'])) 
            item['rise_rate'] = house.xpath('div[@class="priceooo"]/ul/text()').extract()[0]
            item['desc'] = "".join(house.xpath('div[@class="content"]/p[@class="clearfix"]/text()').extract())
            item['contact'] = house.xpath('div[@class="content"]/p[@class="clearfix"]/a/@href').extract()[0]
            item['tag'] = ",".join(house.xpath('div[@class="content"]/ol/label/text()').extract())
            yield item
            #print hid, title, date, price, unit_price, rise_rate, desc, contact, tag
            
        for url in sel.xpath('//div[@class="fanye"]/ul/a/@href').extract():
            yield Request(Settings().get('HOMELINK_URL_PREFIX') + url, callback=self.parse_item)

