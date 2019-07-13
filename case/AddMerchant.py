# coding：utf-8
#author：jiguobin
import random
import string

from selenium.webdriver.common.by import By as by

from base.ActionMethod import ActionMethod as am
from base.PublicBase import Public



class AddMerchant(am):
    def __init__(self,sheet,row):
        self.sheet=sheet
        self.data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))
        print(self.data)

    #流程
    def main(self):
        print(self.data)
        Public.login_ms(self,url=self.data['环境'],name=self.data['账号'],password=self.data['密码'])#登录
        self.type()
        self.merchantInfo()

    def type(self):
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[2]/a')
        self.switch_frame('contframe')
        self.sleep_time(3)
        if self.data['商户类型']=='单店商户':
            self.click(by.XPATH,'/html/body/div[1]/div[2]/div[2]/a[1]')
        else:
            self.click(by.XPATH,'/html/body/div[1]/div[2]/div[2]/a[2]')

    def merchantInfo(self):
        if self.data['商户名称']=='商户' and self.data['商户简称']=='商户':
            self.input(by.ID,'fullNameCn',self.data['商户名称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
            self.input(by.ID,'nameCn',self.data['商户简称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
        else:
            self.input(by.ID,'fullNameCn',self.data['商户名称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
            self.input(by.ID,'nameCn',self.data['商户简称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form[2]/div[1]/div[3]/div/div[1]/div[1]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户省'])
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form[2]/div[1]/div[3]/div/div[1]/div[2]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户市'])
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form[2]/div[1]/div[3]/div/div[1]/div[3]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户区'])
        self.click(by.ID,'easyui-textbox-simple')
        self.input(by.ID,'searchplace',self.data['商户详细地址'])
        self.click(by.ID,'search')
        self.click(by.ID,'saveAddress')
        self.click(by.ID,'selectTrade')
        self.click(by.LINK_TEXT,self.data['所属行业'])
        self.click(by.ID,'noSelectSalesman')
        self.click(by.LINK_TEXT,self.data['业务员'])
        self.input(by.ID,'contactName',self.data['联系人姓名'])
        self.input(by.ID,'contactPhone',self.data['联系人手机'])
        self.input(by.ID,'contactEmail',self.data['联系人邮箱'])
        # self.click(by.LINK_TEXT,self.data['商户版本'])
        self.input(by.ID,'loginNameText',self.data['登录名']+''.join(random.sample(string.ascii_letters+string.digits,2)))
        self.input(by.ID,'passWord',self.data['登录密码'])
        self.input(by.ID,'confirmPassWord',self.data['确认密码'])
        self.click(by.ID,'save')
        self.sleep_time(3)
        self.click(by.XPATH,'/html/body/div[5]/div[2]/a[1]')






#
a=AddMerchant('新增商户',7)
a.main()


