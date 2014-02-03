# -*- coding: utf-8 -*-
# Scrapy settings for homelink project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'homelink'

SPIDER_MODULES = ['homelink.spiders']
NEWSPIDER_MODULE = 'homelink.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36'
COOKIES_DEBUG = False

HOMELINK_USERNAME = "XXXX"
HOMELINK_PASSWORD = "XXXX"
HOMELINK_DOMAIN = "beijing.homelink.com.cn"
HOMELINK_URL_PREFIX = "http://beijing.homelink.com.cn/"
HOMELINK_LOGIN_URL = 'http://beijing.homelink.com.cn/webregister/login.php'
HOMELINK_START_URL = "http://beijing.homelink.com.cn/sold/c1111027378318/pg1rs铭科苑/"

ITEM_PIPELINES = {
    'homelink.pipelines.DuplicatesPipeline': 300
}
