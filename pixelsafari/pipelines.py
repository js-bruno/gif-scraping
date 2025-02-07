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

class PixelsafariGifDownloaderPipeline:
    def open_spider(self, item, spider):
        pass

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



class PixelsafariSqlitePipeline:
    def open_spider(self, item, spider):
        self.conn = sqlite3.connect('db.sqlite3')
    
    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite master where type = "table" and name = "gif"'
        )
        try:
            value = naxt(result)
        except StopIteration as exc:
            self.conn.execute(
                'create table cars(id interger primary key, name text, path text, created_at datetime)'
            )

             
    def close_spider(self, item, spider):
        self.conn.close()

