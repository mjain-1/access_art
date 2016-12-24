# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class showItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    brief_descript = scrapy.Field()
    venue = scrapy.Field()
    dates = scrapy.Field()
    location = scrapy.Field()
    full_descript = scrapy.Field()
    image = scrapy.Field()


class artnetItem(scrapy.Item):
    title = scrapy.Field()
    venue = scrapy.Field()
    dates = scrapy.Field()
    location = scrapy.Field()
    full_descript = scrapy.Field()
    image = scrapy.Field()
    
    
class newyorkerItem(scrapy.Item):
    title = scrapy.Field()
    venue = scrapy.Field()
    dates = scrapy.Field()
    location = scrapy.Field()
    full_descript = scrapy.Field()
    

class artbeatItem(scrapy.Item):
    title = scrapy.Field()
    venue = scrapy.Field()
    dates = scrapy.Field()
    location = scrapy.Field()
    brief_descript = scrapy.Field()
    full_descript = scrapy.Field()
    image = scrapy.Field()
    artist = scrapy.Field()