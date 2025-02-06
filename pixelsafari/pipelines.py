from urllib import request
from pathlib import Path
import os 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

ROOT_DIRECTORY = Path("public")

class PixelsafariPipeline:
    def process_item(self, item, spider):
        folder  = ROOT_DIRECTORY/ item.get("folder") 
        sources = item.get("sources") 

        if not os.path.isdir(folder):
            os.makedirs(folder)

        for source in sources: 
            uri = source.split("/")
            uri.reverse()
             
            response = request.urlopen(source)
            image = response.read()
            
            save_dir = folder / uri[0]


            print(f"Writing -> {save_dir}")
            with open(save_dir, "wb") as file:
                file.write(image)

