# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from Second_House.items import SecondHouseItem

class SecondHouseSpider(scrapy.Spider):
    #定义爬虫名称
    name = 'second_house'

    # 允许的域名
    allowed_domains = ['bj.lianjia.com']

    start_urls = ['http://bj.lianjia.com/ershoufang']

    # 定义一个列表来存储页的网址
    url_list = []

    # 逐页爬取数据，链家一共100页，
    for i in range(1, 101):
        url = 'http://bj.lianjia.com/ershoufang/pg{}'.format(str(i))
        url_list.append(url)

    start_urls = url_list


    #循环遍历100页网址的函数
    def start_requests(self):
        #遍历100页的网址，一页页处理
        for url in self.start_urls:

            #url: 就是需要请求，并进行下一步处理的url,callback: 指定该请求返回的Response，由那个函数来处理。
            yield scrapy.Request(url,callback=self.Url)
            # print(type(url))

    #处理一页当中的房源列表，处理每个标签的链接
    def Url(self,response):
        # print(response.status)
        #selector进行去广告操作，只匹配出需要的HTML
        selector = Selector(response)
        companies = selector.xpath('.//ul[@class="sellListContent"]/li[contains(@class,"clear")]')
        #print(len(companies))

        #循环遍历每页每个房源标签链接
        for company in companies:
            companies = company.xpath('./div/div/a/@href').extract_first()
            # temp.append(url)
            # print(url)

            #把标签链接返回给parse()函数进行处理操作
            yield scrapy.Request(companies,callback=self.parse)

    def parse(self, response):

        item = SecondHouseItem()

        #爬取房源列表信息XPATH
        divs_item = response.xpath('.//div[@class="overview"]')

        # extract_first()：提取符合筛选条件的第一个结果 返回值为unicode字符串
        # extract()：提取符合筛选条件的结果的集合 返回值为unicode字符串列表
        #定义房子标签
        item['Title'] = divs_item.xpath('./div[2]/div[5]/div/a/text()').extract_first()

        #定义价格
        item['Price'] = divs_item.xpath('./div[2]/div[3]/span/text()').extract_first()

        #定义房屋户型
        item['Apartment_layout'] = divs_item.xpath('./div[2]/div[4]/div/div[1]/text()').extract_first()

        #定义房屋朝向
        item['Floor'] = divs_item.xpath('./div[2]/div[4]/div/div[2]/text()').extract_first()

        #定义房屋平米价格
        item['Unit_price'] = divs_item.xpath('./div[2]/div[3]/div/div/span/text()').extract_first()

        #定义房屋面积
        item['Area'] = divs_item.xpath('./div[2]/div[4]/div[3]/div[1]/text()').extract_first()

        #定义小区地址
        item['Address'] = divs_item.xpath('./div[2]/div[5]/div[2]/span[2]/a/text()').extract_first()

        #在parse函数中，将提取出来的结果组合成字典返回
        yield item

