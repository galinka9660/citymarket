# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
""" import psycopg2


class MyScraperPipeline:
    def process_item(self, item, spider):
        return item

class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'G5405524g',
            database = 'test',
            port = "5432"
        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        try:
            self.curr.execute("""# insert into parsed_data (product_name) values (%s)""", (
  #              item["title"]
   #         ))
    #    except BaseException as e:
     #       print(e)
      #  self.connection.commit()
