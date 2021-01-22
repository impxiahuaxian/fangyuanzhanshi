# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import csv


class SecondHousePipeline(object):
    #定义-创建csv文件函数
    def __init__(self):

        #打开文件，newline表示换行标志，取值一般是 None，这样就不会数据总是隔行输入了
        self.file = open('BeiJing_House.csv','a+',encoding="utf-8",newline='')
        print("创建成功")

        # csv写法
        self.writer = csv.writer(self.file)

        #定义标题
        headers = ['Title','Price','Apartment_layout','Area','Floor','Address','Unit_price']

        #插入一行标题
        self.writer.writerow(headers)


    def process_item(self, item, spider):
        #循环写入
        self.writer.writerow((item['Title'],item['Price'],item['Apartment_layout'],item['Area'],
                              item['Floor'],item['Address'],item['Unit_price']))
        print("写入成功")

        # 数据库链接信息
        con = pymysql.connect \
                (
                host="localhost",
                user="root",
                password="19980526",
                port=3306,
                database="Second_House",
                charset="utf8",
                use_unicode=False,

            )
        print("连接成功")
        dbObject = con
        cursor = dbObject.cursor()
        cursor.execute("USE Second_House")

        #SQL语句进行插入数据
        sql = "INSERT INTO BJ_Second_House(Title,Price,Apartment_layout,Area,Floor,Address,Unit_price) " \
              "VALUES" \
              " (%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql,(item['Title'],item['Price'],item['Apartment_layout'],item['Area'],
                               item['Floor'],item['Address'],item['Unit_price']))

        # 提交到数据库执行
        cursor.connection.commit()

        #关闭游标

        #关闭数据库

        return item

    #定义关闭函数
    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
