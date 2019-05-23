# coding：utf-8
#author：jiguobin
from base.ActionMethod import ActionMethod as am
from selenium.webdriver.common.by import By as by
from base.PublicBase import Public
import random
import string
import datetime


class AddStore(am):
    def __init__(self,sheet,row):
        self.sheet=sheet
        self.data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))
        print(self.data)

    #流程
    def main(self):
        print(self.data)
        Public.login_ms(self,url=self.data['环境'],name=self.data['账号'],password=self.data['密码'])#登录
        self.type()
        self.storeInfo()

    def type(self):
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[3]/a')
        self.switch_frame('contframe')
        self.sleep_time(3)
        self.click(by.ID,'add')
        #弹出商户名称处理
        self.input(by.ID,'searchContent',self.data['商户名称'])
        self.click(by.ID,'searchContent')
        self.keys(by.ID,'searchContent')

        self.sleep_time(1.5)
        self.click(by.XPATH,'/html/body/div/div[3]/div[1]/div[2]/div/ul/li')
        self.click(by.ID,'nextStep')

    def storeInfo(self):
        if self.data['门店名称']=='门店' and self.data['门店简称']=='门店':
            self.input(by.ID,'storeFullNameCn',self.data['门店名称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
            self.input(by.ID,'storeNameCn',self.data['门店简称']+''.join(random.sample(string.ascii_letters+string.digits,2)))
        else:
            self.input(by.ID,'storeFullNameCn',self.data['门店名称'])
            self.input(by.ID,'storeNameCn',self.data['门店简称'])
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[3]/div/div[1]/div[1]/div/a/label')
        self.click(by.LINK_TEXT,self.data['门店省'])
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[3]/div/div[1]/div[2]/div/a/label')
        self.click(by.LINK_TEXT,self.data['门店市'])
        self.click(by.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[3]/div/div[1]/div[3]/div/a/label')
        self.click(by.LINK_TEXT,self.data['门店区'])
        self.click(by.ID,'easyui-textbox-simple')
        self.input(by.ID,'searchplace',self.data['门店详细地址'])
        self.click(by.ID,'search')
        self.click(by.ID,'saveAddress')
        self.click(by.ID,'noSelectSalesman')
        self.click(by.LINK_TEXT,self.data['业务员'])
        self.input(by.ID,'contactName',self.data['联系人姓名'])
        self.input(by.ID,'contactPhone',self.data['联系人手机'])
        self.input(by.ID,'contactEmail',self.data['联系人邮箱'])
        self.input(by.ID,'loginNameText',self.data['登录名']+''.join(random.sample(string.ascii_letters+string.digits,2)))
        self.input(by.ID,'passWord',self.data['登录密码'])
        self.input(by.ID,'confirmPassWord',self.data['确认密码'])
        self.click(by.ID,'save')
        self.sleep_time(3)
        self.click(by.CLASS_NAME,'alert_btn alert_btn_cancel')

# a=AddStore('新增门店',2)
# a.main()



