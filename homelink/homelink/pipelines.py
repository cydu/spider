# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['hid'] in self.ids_seen or not item['price']:
            raise DropItem("Duplicate item found: %s" % item['hid'])
        else:
            self.ids_seen.add(item['hid'])
            return item
