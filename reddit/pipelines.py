# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RedditPipeline(object):
    def process_item(self, item, spider):
        item['title'] = ''.join(item['title']).upper()
        return item

import MySQLdb
import string

class MySQLPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, dbu, dbp, dbh, db):
        self.dbu = dbu
        self.dbp = dbp
        self.dbh = dbh
        self.db = db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            dbu=crawler.settings.get('DBU'),
            dbp=crawler.settings.get('DBP'),
            dbh=crawler.settings.get('DBH'),
            db=crawler.settings.get('DB')
        )

    def open_spider(self, spider):
        self.conn = MySQLdb.connect(self.dbh,self.dbu,self.dbp,self.db)
        self.c = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()
        self.client.close()

    def insert_news(self,spider,title,url,dateretrieved):
        try:
            self.c.execute("SELECT COUNT(*) FROM "+self.db+".reddit WHERE url = '"+url+"'") #Check if article is already here
            count = self.c.fetchone()
            if count[0] == 0:
                self.c.execute('''INSERT INTO '''+self.db+'''.reddit (type,headline,url,dateretrieved) VALUES (%s,%s,%s,%s)''',[spider.name,title,url,dateretrieved])
        except:
            print "OMG AN ERROR!!!!"
        #    pass

    def process_item(self, item, spider):  
        
        title=item['title'].encode('utf-8').replace("'",'')
        try:
            url=item['url'].encode('utf-8')
        except AttributeError:
            url=item['url'][0].encode('utf-8')
        dateretrieved=item['timeretrieved'].encode('utf-8')
        self.insert_news(spider,title,url,dateretrieved)
        self.conn.commit()
        return item