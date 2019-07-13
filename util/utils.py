# -*- coding: utf-8 -*- 
# @Time : 2019/7/6 11:22 
# @Author : Ji
# @File : utils.py 
class Utils():
    #判断元素是否存在
    def isElementExist(self,type,element):
        flag=True
        browser=self.driver
        try:
            if type == "xpath":
                browser.find_element_by_xpath(element)
            elif type == "class name":
                browser.find_element_by_class_name(element)
            elif id=='id':
                browser.find_element_by_id(element)
            return flag

        except:
            flag=False
            return flag


