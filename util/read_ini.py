#coding=utf-8
#author：jiguobin


import configparser

#重构封装
class ReadIni(object):
     # 构造函
    def __init__(self,file_name=None,node=None):
        '''
        :param file_name:配置文件地址
        :param node: 节点名
        '''
        #容错处理
        if file_name == None:
            #默认地址
            file_name = 'D:\liantuo\python\config\element.ini'
        else:
            self.file_name=file_name
        if node == None:
            #默认节点
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

#
if __name__ == '__main__':
    # #自定义
    # path=r'E:\Pythonx\seleniumTest\config\testIni.ini'
    # read_init = ReadIni(node='menu')   #传入新自定义配置文件地址、节点
    # print(read_init.get_value('shanghu'))                   #获取value值
    #默认
    read_init = ReadIni()   #默认配置文件地址、节点
    print(read_init.get_value('user_name'))  #获取value值



