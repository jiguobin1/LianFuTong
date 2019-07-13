# -*- coding: utf-8 -*- 
# @Time : 2019/7/10 18:01 
# @Author : Ji
# @File : TwoLs.py
from selenium.webdriver.common.by import By as by
from base.ActionMethod import ActionMethod as am
from base.PublicBase import Public

class TwoLs(am):
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

    #选择通道
    def aisleInfo(self):
        self.click(by.ID,'toYeahkaForZeroRate')
        #输入配置名称
        if self.data['配置名称'] !='':
            self.clear(by.ID,'configureName')
            self.input(by.ID,'configureName',self.data['配置名称'])
        #选择通道名称
        self.click(by.ID,'noSelcetPassTypeName')
        self.click(by.LINK_TEXT,self.data['通道名称'])
        self.sleep_time(0.5)
       #如果费率不存在则不选
        if self.data['支付宝费率名称']!='':
            self.click(by.ID,'noSelcetAlipayRateName')
            self.click(by.LINK_TEXT,self.data['支付宝费率名称'])   #支付宝费率名称
        if self.data['微信费率名称']!='':
            self.click(by.ID,'noSelcetWechatRateName')
            self.click(by.LINK_TEXT,self.data['微信费率名称'])   #微信费率名称
        #输入配置备注
        self.input(by.ID,'configureRemark',self.data['配置备注'])

    def merchantInfo(self):
        self.clear(by.ID,'fullNameCn')
        self.input(by.ID,'fullNameCn',self.data['商户名称'])
        self.click(by.ID,'next')
        self.input(by.ID,'nameCn',self.data['商户简称'])
        self.input(by.ID,'file0',self.data['营业执照照片'])
        self.input(by.ID,'businessLicenseNo',self.data['营业执照编号'])
        self.input(by.ID,'businessLicenseFullName',self.data['营业执照注册名称'])
        self.input(by.ID,'businessLicenseAddress',self.data['营业执照注册地址'])
        #营业执照时间
        self.click(by.ID,'businessStartDate')
        self.click(by.CLASS_NAME,'kui_year_select')
        self.click(by.XPATH,'/html/body/div[4]/div/div[1]/select[1]/option[89]')
        self.click(by.CLASS_NAME,'kui_month_select')
        self.click(by.XPATH,'/html/body/div[4]/div/div[1]/select[2]/option[4]')
        self.click(by.XPATH,'/html/body/div[4]/div/div[2]/table/tbody[2]/tr[2]/td[4]')
        self.click(by.ID,'timelongbtn3')
        #商户所属地区
        self.click(by.XPATH,'/html/body/form[2]/div[2]/div/div[2]/div[7]/div[1]/div[1]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户省'])
        self.click(by.XPATH,'/html/body/form[2]/div[2]/div/div[2]/div[7]/div[1]/div[2]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户市'])
        self.click(by.XPATH,'/html/body/form[2]/div[2]/div/div[2]/div[7]/div[1]/div[3]/div/a/label')
        self.click(by.LINK_TEXT,self.data['商户区'])
        self.clear(by.ID,'address')
        self.clear(by.ID,'address')
        self.input(by.ID,'address',self.data['商户详细地址'])
        self.input(by.ID,'mobile',self.data['联系人手机号码'])
        self.input(by.ID,'customerPhone',self.data['客服电话'])
        self.input(by.ID,'file1',self.data['身份证国徽面'])
        self.input(by.ID,'file2',self.data['身份证人像面'])
        self.input(by.ID,'companyCorporation',self.data['法人姓名'])
        self.input(by.ID,'certificateHolderNo',self.data['法人证件号码'])
        self.input(by.ID,'file3',self.data['负责人与门头合照'])
        self.input(by.ID,'file4',self.data['经营场所内设照片'])
        #如果费率不存在则不选
        if self.data['支付宝费率名称']!='':
            self.input(by.ID,'file5',self.data['支付宝收银台照片'])
        if self.data['微信费率名称']!='':
            self.input(by.ID,'file6',self.data['微信收银台照片'])
        self.input(by.ID,'file7',self.data['第三方平台入驻照片'])
        self.sleep_time(2.5)
        self.click(by.ID,'next1')

    def bankInfo(self):
        if self.sheet[4:]=='个人':
            self.click(by.ID,'noSelectAccountType')
            self.click(by.LINK_TEXT,'个人')
            if self.sheet[4:]=='个人' and self.data['结算人类型']=='非法人':
                print('走到这了么')
                self.click(by.ID,'noSelectLegalFlag')
                self.click(by.LINK_TEXT,'非法人')
                self.input(by.ID,'legalFlagCardNo',self.data['非法人证件号码'])
                self.input(by.ID,'file9',self.data['非法人国徽面'])
                self.input(by.ID,'file10',self.data['非法人人像面'])
                self.input(by.ID,'file11',self.data['非法人结算授权图片'])
        #开户银行所在城市
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[6]/div[1]/div[1]/div/a/label')
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[6]/div[1]/div[1]/div/dl/dd[16]/a')
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[6]/div[1]/div[2]/div/a/label')
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[6]/div[1]/div[2]/div/dl/dd[4]/a')
        #开户银行
        self.input(by.ID,'bankName',self.data['开户银行'])
        self.sleep_time(0.5)
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[7]/div[1]/dl/dd')
        #弹出开户支行名称处理
        self.input(by.ID,'branch',self.data['开户支行名称'])
        self.click(by.ID,'branch')
        self.keys(by.ID,'branch')
        self.sleep_time(1)
        self.click(by.XPATH,'/html/body/form[2]/div[3]/div/div[2]/div[16]/div/ul/li[1]')
        #银行卡照片
        self.input(by.ID,'file8',self.data['银行卡正面照片'])
        if self.sheet[4:]=='企业':
            self.input(by.ID,'cardNo',self.data['对公账户'])
            self.input(by.ID,'accountHolder',self.data['企业名称'])
        else:
            self.input(by.ID,'cardNo',self.data['银行卡号'])
            self.input(by.ID,'accountHolder',self.data['开户人'])
        self.input(by.ID,'accountHolderMobile',self.data['银行预留手机号'])


l=TwoLs('乐刷千二个人',2)
l.main()



















