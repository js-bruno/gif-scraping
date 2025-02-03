from urllib import request
import os 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class PixelsafariPipeline:
    def process_item(self, item, spider):
        folder  = "./" + item.get("folder") 
        sources = item.get("sources") 
        if not os.path.isdir(folder):
            os.makedirs(folder)

        for source in sources: 
            uri = source.split("/")
            uri.reverse()
             
            request.urlretrieve(source, folder+"/"+uri)
