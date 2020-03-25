# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ConstellationsPipeline(object):
    
    def open_spider(self, spider):
        self.conn = sqlite3.connect('constellations.sqlite')
        self.cur = self.conn.cursor()
        #self.cur.execute('delete from constellations')
        self.cur.execute('''create table if not exists
                            constellations(name        varchar(20),
                                           date        varchar(20),
                                           whole_star  text,
                                           whole_desc  text,
                                           love_star   text,
                                           love_desc   text,
                                           work_star   text,
                                           work_desc   text,
                                           money_star  text,
                                           money_desc  text)
                         ''')
    
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
    
    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into constellations({}) values({})'
        self.cur.execute(sql.format(col, placeholders), tuple(item.values()))
        #print(tuple(item.values()))
        return item
