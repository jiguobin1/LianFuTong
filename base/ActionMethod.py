#coding=utf-8
#author：jiguobin
# from util1 import FindElement
from selenium import webdriver
import time
import xlrd
import os
from selenium.webdriver.common.keys import Keys
class ActionMethod():
    def __init__(self):
        pass
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #切换frame
    def switch_frame(self,frame):
        self.driver.switch_to.frame(frame)
        self.sleep_time(2)

    #等待
    def sleep_time(self,times):
        time.sleep(times)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()

    #获取title
    def get_title(self):
        title = self.driver.title
        return title

    #定位元素
    def get_element(self,node,key):
        read_ini=ReadIni(node=node)
        data=read_ini.get_value(key)
        by=data.split('>')[0]   #定位方式
        value=data.split('>')[1]  #定位值
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by =='className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'text':
                return self.driver.find_element_by_link_text(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

    #清空文本
    def clear(self,type,value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "class name":
            self.driver.find_element_by_class_name(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    #键盘事件keys
    def keys(self,type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(Keys.BACK_SPACE)
        elif type == "class name":
            self.driver.find_element_by_class_name(value).send_keys(Keys.BACK_SPACE)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(Keys.BACK_SPACE)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(Keys.BACK_SPACE)
        elif type == "link text":
            self.driver.find_element_by_link_text(value).send_keys(Keys.BACK_SPACE)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(Keys.BACK_SPACE)

    #输入
    def input(self, type, value, inputvalue):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)

     # 鼠标事件方法

    #点击事件
    def click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "class name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial link text":
            self.driver.find_element_by_partial_link_text(value).click()



    #读取excel
    def get_excel_value(self,sheet,row,file_name=None):
        '''
        :param file_name:打开excel
        :param sheet: 获取页数
        :param row:
        '''
        if file_name == None:
            #默认地址
            # file_name = os.path.dirname(os.path.abspath('.'))+'\data\excel\ks_info.xlsx'
            file_name = 'D:\\liantuo\\LianFuTong\\data\excel\\ks_info.xlsx'
            print(file_name)
        else:
            self.file_name=file_name
        book = xlrd.open_workbook(file_name) #打开一个excel
        sheet = book.sheet_by_name(sheet)
        data=sheet.row_values(row)
        return data









