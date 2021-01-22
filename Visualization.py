import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time



class visualization():
    def __init__(self):
        #读取房源文件
        self.House_data = pd.read_csv(r'F:\TSU\Second_House\BeiJing_House.csv')


        plt.rcParams['font.sans-serif']=['SimHei']#中文设置
        plt.rcParams['axes.unicode_minus'] = False#正常显示负号
        plt.rcParams['lines.color'] = 'red'#设置线条颜色

        self.H_address()
        self.H_type()
        self.H_unit()


    #可视化各个地区房源数量
    def H_address(self):
        House_address = self.House_data['Address'].value_counts()
        # print(House_address)

        #设置画布
        asd, sdf = plt.subplots(1, 1, dpi=200)
        House_address.plot(kind='bar', x='House_address', y='size', title='北京各个地区的房源数量分布信息',
                           color=['green', 'red', 'blue', 'grey', 'pink'], ax=sdf)
        plt.legend(['各个地区房源数量'])
        print("可视化各个地区房源数量分析完成,即将保存结果")
        time.sleep(1)
        for i in range(1,4):
            print(i)
            time.sleep(1)
        #保存图片
        if os.access("F:\TSU\Second_House\image\House_address.jpg",os.F_OK):
            print("已经存在House_address.jpg文件")
        else:
            plt.savefig(r'F:\TSU\Second_House\image\House_address.jpg', bbox_inches='tight')
            print("保存完毕")


    #可视化户型数量
    def H_type(self):
        House_type = self.House_data['Apartment_layout'].value_counts()
        asd, sdf = plt.subplots(1, 1, dpi=200)
        House_type.plot(kind='bar', x='House_type', y='size', title='户型数量', color=['green', 'red', 'blue', 'grey', 'pink'],
                        ax=sdf)
        plt.legend(['数量'])
        print("可视化户型数量分析完成,即将保存结果")
        time.sleep(1)
        for i in range(1,4):
            print(i)
            time.sleep(1)
        if os.access("F:\TSU\Second_House\image\House_type.jpg",os.F_OK):
            print("已经存在House_type.jpg文件")
        else:
            plt.savefig(r'F:\TSU\Second_House\image\House_type.jpg', bbox_inches='tight')
            print("保存完毕")

    #可视化各个地区房源均价
    def H_unit(self):
        House_unit = self.House_data.groupby('Address').mean()['Unit_price']
        asd,sdf = plt.subplots(1,1,dpi=200)
        House_unit.plot(x='House_unit',y = 'size',title='北京各个地区房源均价',color='red',ax=sdf)
        plt.grid(linestyle=":", color="r")
        plt.legend(['房源均价'])
        print("可视化各个地区房源均价分析完成,即将保存结果")
        time.sleep(1)
        for i in range(1,4):
            print(i)
            time.sleep(1)
        if os.access("F:\TSU\Second_House\image\House_unit.jpg", os.F_OK):
            print("已经存在House_unit.jpg文件")
        else:
            plt.savefig(r'F:\TSU\Second_House\image\House_unit.jpg', bbox_inches='tight')
            print("保存完毕")

if __name__ == '__main__':
    test = visualization()

