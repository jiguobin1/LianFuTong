#coding=utf-8
#author：jiguobin
from selenium.webdriver.common.by import By as by

from base.ActionMethod import ActionMethod as am
from base.PublicBase import Public


class LsPage(am):
    def __init__(self,sheet,row):
        self.sheet=sheet
        self.data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))


    def main(self):
        print(self.data)
        Public.login_ms(self,url=self.data['环境'],name=self.data['账号'],password=self.data['密码'])#登录
        Public.merchantType(self,'ls')
        self.aisleInfo()
        self.merchantInfo()
        self.bankInfo()
        self.imageInfo()


     #选择通道
    def aisleInfo(self):
        #输入配置名称
        if self.data['配置名称'] !='':
            self.clear(by.ID,'configureName')
            self.input(by.ID,'configureName',self.data['配置名称'])
        #选择通道名称
        self.click(by.ID,'noSelcetPassTypeName')
        self.click(by.LINK_TEXT,self.data['通道名称'])
        self.sleep_time(0.5)
        #选择支付宝费率
        self.click(by.ID,'noSelcetAlipayRateName')
        self.click(by.LINK_TEXT,self.data['支付宝费率名称'])
        #选择微信费率
        self.click(by.ID,'noSelcetWechatRateName')
        self.click(by.LINK_TEXT,self.data['微信费率名称'])
        #输入配置备注
        self.input(by.ID,'configureRemark',self.data['配置备注'])


     #商户信息
    def merchantInfo(self):
        self.clear(by.ID,'nameCn')
        self.input(by.ID,'nameCn',self.data['商户简称'])
        self.click(by.ID,'tradechoisecont')
        #经营类目
        self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[2]/div[1]/div/div/dl[3]/dd[1]')
        # self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[2]/div[1]/div/div/dl[2]/dd[2]')
        # self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[2]/div[1]/div/div/dl[3]/dd[26]')
        self.input(by.ID,'companyCorporation',self.data['法人姓名'])
        self.input(by.ID,'certificateHolderNo',self.data['法人证件号码'])
        self.input(by.ID,'mobile',self.data['联系人手机号码'])
        self.input(by.ID,'customerPhone',self.data['客服电话'])
        #商户所属地区  门店有问题
        if self.data['门店id']!='':
            self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[8]/div[1]/div[1]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户省'])
            self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[8]/div[1]/div[2]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户市'])
            self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[8]/div[1]/div[3]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户区'])
        else:
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[8]/div[1]/div[1]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户省'])
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[8]/div[1]/div[2]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户市'])
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[8]/div[1]/div[3]/div/a/label')
            self.click(by.LINK_TEXT,self.data['商户区'])

        self.clear(by.ID,'address')
        self.input(by.ID,'address',self.data['商户详细地址'])
        self.input(by.ID,'businessLicenseNo',self.data['营业执照编号'])
        self.input(by.ID,'businessLicenseFullName',self.data['营业执照注册名称'])
        self.input(by.ID,'businessLicenseAddress',self.data['营业执照注册地址'])
        #营业执照注册时间
        # self.click(by.ID,'businessStartDate')
        # self.click(by.XPATH,'/html/body/div[3]/div/div[1]/select[1]')
        # self.click(by.XPATH,'/html/body/div[5]/div/div[1]/select[1]/option[89]')
        # self.click(by.XPATH,'/html/body/div[5]/div/div[1]/select[1]/option[89]')
        # self.click(by.XPATH,'/html/body/div[5]/div/div[1]/select[2]')
        # self.click(by.XPATH,'/html/body/div[5]/div/div[1]/select[2]/option[4]')
        # self.click(by.XPATH,'/html/body/div[5]/div/div[2]/table/tbody[2]/tr[2]/td[4]')
        # self.click(by.ID,'timelongbtn3')


    def bankInfo(self):
        self.click(by.ID,'noSelectAccountType')
        #账户类型
        self.click(by.LINK_TEXT, self.sheet[2:])
        self.click(by.ID,'noSelectLegalFlag')
        self.click(by.LINK_TEXT,self.data['结算人类型'])
        #北京省北京市同一个值 text定位不到
        if self.data['开户省']=='北京':
            if self.data['门店id']!='':
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[1]/div/a/label')
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[1]/div/dl/dd[2]/a')
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[2]/div/a/label')
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[2]/div/dl/dd[2]/a')
            else:
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[1]/div/a/label')
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[1]/div/dl/dd[2]/a')
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[2]/div/a/label')
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[2]/div/dl/dd[2]/a')
        else:
            if self.data['门店id']!='':
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[1]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户省'])
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div[1]/div[18]/div/div[1]/div/div[2]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户市'])
            else:
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[1]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户省'])
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[1]/div/div[2]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户市'])
        self.input(by.ID,'bankName',self.data['开户银行'])
        self.sleep_time(0.5)

        if self.data['门店id']!='':
            self.click(by.XPATH,'/html/body/div/form/div[4]/div[1]/div[18]/div/div[2]/div[1]/dl/dd')
        else:
            self.click(by.XPATH,'/html/body/div/form[3]/div[4]/div[1]/div[18]/div/div[2]/div[1]/dl/dd')

        #弹出开户支行名称处理
        self.input(by.ID,'branch',self.data['开户支行名称'])
        self.click(by.ID,'branch')
        self.keys(by.ID,'branch')
        self.sleep_time(1)
        if self.data['门店id']!='':
           self.click(by.XPATH,'/html/body/div/form/div[4]/div[1]/div[18]/div/div[4]/div/ul/li')
        else:
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div/div[4]/div/ul/li')
        self.input(by.ID,'accountHolder',self.data['开户人'])
        self.input(by.ID,'cardNo',self.data['银行卡号'])
        self.input(by.ID,'accountHolderMobile',self.data['银行预留手机号'])

    def imageInfo(self):
        self.input(by.ID,'file1',self.data['人像面'])
        self.input(by.ID,'file2',self.data['国徽面'])
        self.input(by.ID,'file3',self.data['银行卡正面照'])
        self.input(by.ID,'file4',self.data['营业执照'])
        self.input(by.ID,'file5',self.data['经营场所内设照'])
        self.input(by.ID,'file6',self.data['门头照'])
        self.input(by.ID,'file7',self.data['收银台照'])













# l=LsPage('乐刷个人',4)
# l.main()







