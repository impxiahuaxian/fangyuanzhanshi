# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SecondHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Title = scrapy.Field()  #房屋标签

    Price = scrapy.Field()  #房屋价格

    Apartment_layout = scrapy.Field()   #房屋户型

    Floor = scrapy.Field()  #房屋朝向

    Unit_price = scrapy.Field() #房屋平米价格

    Area = scrapy.Field()   #房屋面积

    Address = scrapy.Field()    #小区地址