#coding=utf-8
#author：jiguobin
import random
import string

from selenium.webdriver.common.by import By as by

from base.ActionMethod import ActionMethod as am
from base.PublicBase import Public


class WsPage(am):
    def __init__(self,sheet,row):
        self.sheet=sheet
        self.data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))
        print(self.data)

    def main(self):
            Public.login_ms(self,url=self.data['环境'],name=self.data['账号'],password=self.data['密码'])#登录
            Public.merchantType(self,'ws')
            self.aisleInfo()
            self.merchantInfo()
            self.bankInfo()
            self.imageInfo()

     #选择通道
    def aisleInfo(self):
        #走千二通道
        if self.data['通道类型']=='千二':
            self.click(by.XPATH,'/html/body/form[3]/div[1]/div[2]/div/a[2]')
            self.sleep_time(0.5)
        #配置名称可空
        if self.data['配置名称'] !='':
            self.clear(by.ID,'configureName')
            self.input(by.ID,'configureName',self.data['配置名称'])
        self.click(by.ID,'noSelcetPassTypeName')
        self.click(by.LINK_TEXT,self.data['通道名称'])  #选择通道名称
        self.sleep_time(0.5)
        #如果费率不存在则不选
        if self.data['支付宝费率名称']!='':
            self.click(by.ID,'noSelcetAlipayRateName')
            self.click(by.LINK_TEXT,self.data['支付宝费率名称'])   #支付宝费率名称
        if self.data['微信费率名称']!='':
            self.click(by.ID,'noSelcetWechatRateName')
            self.click(by.LINK_TEXT,self.data['微信费率名称'])   #微信费率名称
        if self.data['云闪付费率名称']!='':
            self.click(by.ID,'noSelectQuickPassRateName')
            self.click(by.LINK_TEXT,self.data['云闪付费率名称'])   #微信费率名称
        self.input(by.ID,'configureRemark',self.data['配置备注'])
        self.clear(by.ID,'fullNameCn')
        #商户基本信息
        self.input(by.ID,'fullNameCn',self.data['商户名称'])#商户名称
        if self.data['通道类型']!='千二':
            self.click(by.ID,'noSelectBusinessCategory')
            self.click(by.LINK_TEXT,self.data['经营类目']) #经营类型
        if self.sheet=='网商个人':   #判断商户类型
            self.click(by.ID,'shoptype1')
        elif self.sheet=='网商个体':
            self.click(by.ID,'shoptype2')
        else:
            self.click(by.ID,'shoptype3')
        self.click(by.ID,'next')
        self.sleep_time(0.5)

    #商户信息
    def merchantInfo(self):
        self.clear(by.ID,'nameCn')
        self.input(by.ID,'nameCn',self.data['商户简称'])
        #个人没有营业执照编号
        if self.sheet=='网商个体':  #个体的营业执照编号不能重复
            self.input(by.ID,'businessLicenseNo',''.join(random.sample(string.ascii_letters+string.digits,18)))
        elif self.sheet=='网商企业':
            self.input(by.ID,'businessLicenseNo',self.data['营业执照编号'])
        self.click(by.XPATH,'//*[@id="province"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户省'])
        self.click(by.XPATH,'//*[@id="city"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户市'])
        self.click(by.XPATH,'//*[@id="country"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户区'])
        self.clear(by.ID,'address')
        self.input(by.ID,'address',self.data['商户详细地址'])
        if self.data['通道类型']=='千二':
            self.input(by.ID,'principalEmail',self.data['负责人邮箱'])
        self.input(by.ID,'customerPhone',self.data['负责人电话'])
        self.input(by.ID,'contactName',self.data['负责人'])
        self.input(by.ID,'wechatPublicNo',self.data['推荐关注微信APPID'])


    #银行卡信息
    def bankInfo(self):
        self.input(by.ID,'bankName',self.data['开户银行'])
        self.sleep_time(1)
        self.click(by.XPATH,'//*[@id="hotSelect"]/dl/dd')
        self.input(by.ID,'cardNo',self.data['银行卡号'])
        if self.sheet!='网商企业':
            self.input(by.ID,'accountHolder',self.data['开户人'])
            self.input(by.ID,'certificateHolderNo',self.data['身份证号码'])
            self.input(by.ID,'cardholderAddress',self.data['身份证地址'])
        else:
            self.input(by.ID,'companyCorporation',self.data['法人'])
            self.input(by.ID,'certificateNo',self.data['法人证件号'])


    #图片信息
    def imageInfo(self):
        #千二和普通的元素id不一样
        if self.data['通道类型']=='千二' and self.sheet=='网商个体':
            self.input(by.ID,'multipartFile4',self.data['收银台照片'])
            self.input(by.ID,'multipartFile5',self.data['店内环境照'])
            self.input(by.ID,'multipartFile6',self.data['主流餐饮平台认证照片'])
        elif self.data['通道类型']=='千二' and self.sheet=='网商企业':
            self.input(by.ID,'multipartFile4',self.data['收银台照片'])
            self.input(by.ID,'multipartFile5',self.data['店内环境照'])
            self.input(by.ID,'multipartFile6',self.data['主流餐饮平台认证照片'])
            self.input(by.ID,'multipartFile8',self.data['开户许可证'])
        else:
            self.input(by.ID,'multipartFile4',self.data['店内环境照'])
         #个人没有营业执照照片
        if self.sheet!='网商个人':
            self.input(by.ID,'multipartFile0',self.data['营业执照照片'])
        #企业有开户许可证
        if self.sheet=='网商企业':
            self.input(by.ID,'multipartFile6',self.data['开户许可证'])
        self.input(by.ID,'multipartFile1',self.data['人像面照片'])
        self.input(by.ID,'multipartFile2',self.data['国徽面照片'])
        self.input(by.ID,'multipartFile3',self.data['门头照'])



w=WsPage('网商个人',2)
w.main()
