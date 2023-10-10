# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

import mysql.connector


class Amazon2Pipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Pavan1234#.',
            database='amazon'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS amazon_tb""")
        self.curr.execute(""" create table amazon_tb (
                                product_name text,
                                product_age_use text,
                                product_price int
                                product_link text
                                 )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into amazon_tb values (%s,%s,%s,%s)""", (
            str(item['product_name']),
            str(item['product_age_use']),
            str(item['product_price']),
            str(item['product_link'])
        ))
        self.conn.commit()
