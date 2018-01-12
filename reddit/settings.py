# -*- coding: utf-8 -*-

# Scrapy settings for reddit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'reddit'

SPIDER_MODULES = ['reddit.spiders']
NEWSPIDER_MODULE = 'reddit.spiders'

DBU = 'DATABASEUSERNAME'
DBP = 'DATABASEPASSWORD'
DB = 'DATABASE'
DBH = 'localhost'
DBPORT = 3306

USER_AGENT = 'IntelNexus Spider (USER@EXAMPLE.COM)'

FEED_URI = 'logs/%(name)s/%(time)s.csv'
FEED_FORMAT = 'csv'

ITEM_PIPELINES = {
	'reddit.pipelines.RedditPipeline': 100,
    'reddit.pipelines.MySQLPipeline': 200
}

