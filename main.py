from PyQt5 import QtWidgets, QtCore, QtGui
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from scrapy import cmdline
import time



import sys
from UI_show import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class show(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):

        super(show, self).__init__()
        self.setupUi(self)

        #设置窗口的标题
        self.setWindowTitle("二手房爬虫界面")

        # 设置窗口的图标，引用当前目录下的spider.png图片
        self.setWindowIcon(QIcon('spider.jpg'))

        #为界面插入背景图
        self.setStyleSheet("#MainWindow{border-image:url(F:/TSU/Second_House/house.jpg);}")

        #设置透明
        self.setWindowOpacity(1)

        #设置label字体颜色
        self.label_2.setStyleSheet("color:red")
        #设置label背景颜色
        # self.label_2.setStyleSheet("background-color:red")

        #按钮绑定连接
        # self.run_Button.clicked.connect(self.run_spider)
        self.apart_Button.clicked.connect(self.apart_layout)
        self.unit_Button.clicked.connect(self.unit_price)
        self.address_Button.clicked.connect(self.address)
        self.run_view_Button.clicked.connect(self.run_Visualization)


    # #运行爬虫
    # def run_spider(self):
    #     cmdline.execute('scrapy crawl second_house'.split())
    #     # a = visualization()

    #运行数据分析模块
    def run_Visualization(self):
        os.system("python Visualization.py")
        time.sleep(2)
        print("分析完成,结果保存在本地")


    #可视化户型数量
    def apart_layout(self):
        jpg = QtGui.QPixmap("F:\TSU\Second_House\image\House_type.jpg").scaled(self.label.width(),
                                                                                  self.label.height())
        self.label.setPixmap(jpg)
        print("如图显示")

    #可视化各个地区房源均价
    def unit_price(self):
        jpg = QtGui.QPixmap("F:\TSU\Second_House\image\House_unit.jpg").scaled(self.label.width(),
                                                                                  self.label.height())
        self.label.setPixmap(jpg)
        print("如图显示")

    #可视化各个地区房源数量
    def address(self):
        jpg = QtGui.QPixmap("F:\TSU\Second_House\image\House_address.jpg").scaled(self.label.width(),
                                                                                  self.label.height())
        self.label.setPixmap(jpg)
        print("如图显示")

if __name__ == "__main__":
    #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QtWidgets.QApplication(sys.argv)
    my = show()
    my.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())


