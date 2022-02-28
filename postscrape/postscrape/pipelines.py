# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter

class JsonWriterPipeline:
    def open_spider(self, ro):
        self.file = open('ro_items.json', 'w',encoding='utf-8')

    def close_spider(self, ro):
        self.file.close()

    def process_item(self, ro_item, ro):
        line = json.dumps(ItemAdapter(ro_item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return ro_item
