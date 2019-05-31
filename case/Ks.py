# coding=utf-8
#author：jiguobin
from selenium.webdriver.common.by import By as by
from base.ActionMethod import ActionMethod as am
from base.PublicBase import Public



class KsPage(am):
    def __init__(self,sheet,row):
        self.sheet=sheet
        self.data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))
        print(self.data)

    #流程
    def main(self):
        print(self.data)
        Public.login_ms(self,url=self.data['环境'],name=self.data['账号'],password=self.data['密码'])#登录
        Public.merchantType(self,'ks')
        self.aisleInfo()
        self.merchantInfo()
        self.bankInfo()
        self.imageInfo()

    #选择通道
    def aisleInfo(self):
        #判断通道类型
        if self.data['通道类型']=='千二':
            self.click(by.XPATH,'/html/body/div[1]/div[2]/div/a[2]')
            self.sleep_time(0.5)
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
        #输入商户名称
        self.clear(by.ID,'fullNameCn')
        self.input(by.ID,'fullNameCn',self.data['商户名称'])
        #商户简称
        self.clear(by.ID,'nameCn')
        self.input(by.ID,'nameCn',self.data['商户简称'])
        #商户经营类目（普通与企业xpath不同）
        if self.data['通道类型']=='千二':
            self.click(by.CLASS_NAME,'tradechoisecont')
            self.sleep_time(0.5)
            self.click(by.XPATH,'/html/body/div[1]/form[2]/div[4]/div/div[4]/div/div[1]/div/dl[3]/dd')#经营类目
        else:
            self.click(by.CLASS_NAME,'tradechoisecont')
            self.sleep_time(0.5)
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[4]/p/div/dl[3]/dd[1]')
        self.input(by.ID,'customerPhone',str(self.data['客服电话']))
        self.click(by.XPATH,'//*[@id="province"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户省'])
        self.click(by.XPATH,'//*[@id="city"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户市'])
        self.click(by.XPATH,'//*[@id="country"]/a/label')
        self.click(by.LINK_TEXT,self.data['商户区'])
        self.clear(by.ID,'address')
        self.input(by.ID,'address',self.data['商户详细地址'])
        self.input(by.ID,'businessLicenseNo',self.data['营业执照编号'])
        self.input(by.ID,'contactPhone',self.data['联系人电话'])
        self.input(by.ID,'contactEmail',self.data['联系人邮箱'])
        self.input(by.ID,'remark',self.data['备注'])

    #银行卡信息
    def bankInfo(self):
        self.click(by.ID,'noSelectAccountType')
        #账户类型
        self.click(by.LINK_TEXT, self.sheet[2:])
        self.input(by.ID,'bankName',self.data['开户银行'])
        self.sleep_time(1)
        self.click(by.XPATH,'//*[@id="hotSelect"]/dl/dd')
        #个人进件
        if (self.sheet=='客商个人'):
            self.input(by.ID,'cardNo',self.data['银行卡号'])
            self.input(by.ID,'accountHolder',self.data['开户人'])
            self.input(by.ID,'certNo',self.data['身份证号码'])
            self.input(by.ID,'mobile',str(self.data['银行预留手机号']))
        #企业进件
        else:
            #企业千二进件（普通与企业xpath不同）
            if self.data['通道类型']=='千二':
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div/div[16]/div[1]/div[1]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户省'])
                self.click(by.XPATH,'/html/body/div[1]/form/div[4]/div/div[16]/div[1]/div[2]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户市'])
            #企业普通进件
            else:
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div[1]/div[1]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户省'])
                self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div[1]/div[2]/div/a/label')
                self.click(by.LINK_TEXT,self.data['开户市'])
            self.input(by.ID,'subbranchName',self.data['开户支行名称'])
            self.input(by.ID,'cardNo',self.data['银行卡号'])
            self.input(by.ID,'accountHolder',self.data['企业名称'])
            self.input(by.ID,'legalPersonName',self.data['法人姓名'])
            self.input(by.ID,'certNo',self.data['身份证号码'])

     #图片信息
    def imageInfo(self):
        if self.data['通道类型']!='千二':
            if (self.sheet=='客商企业'):
                self.input(by.ID,'file0',self.data['营业执照片'])
                self.input(by.ID,'file1',self.data['人像面照片'])
                self.input(by.ID,'file2',self.data['国徽面照片'])
                self.input(by.ID,'file3',self.data['开户许可证照片'])
            else:
                self.input(by.ID,'file0',self.data['营业执照片'])
                self.input(by.ID,'file1',self.data['人像面照片'])
                self.input(by.ID,'file2',self.data['国徽面照片'])
        else:
            if (self.sheet=='客商企业'):
                self.input(by.ID,'multipartFile0',self.data['人像面照片'])
                self.input(by.ID,'multipartFile1',self.data['国徽面照片'])
                self.input(by.ID,'multipartFile2',self.data['门头照'])
                self.input(by.ID,'multipartFile3',self.data['支付宝收银台照片'])
                self.input(by.ID,'multipartFile4',self.data['微信收银台照片'])
                self.input(by.ID,'multipartFile5',self.data['店内环境照片'])
                self.input(by.ID,'multipartFile6',self.data['营业执照片'])
                self.input(by.ID,'multipartFile7',self.data['主流餐饮平台认证照片'])
                self.input(by.ID,'multipartFile8',self.data['开户许可证照片'])
            else:
                self.input(by.ID,'multipartFile0',self.data['人像面照片'])
                self.input(by.ID,'multipartFile1',self.data['国徽面照片'])
                self.input(by.ID,'multipartFile2',self.data['门头照'])
                self.input(by.ID,'multipartFile3',self.data['支付宝收银台照片'])
                self.input(by.ID,'multipartFile4',self.data['微信收银台照片'])
                self.input(by.ID,'multipartFile5',self.data['店内环境照片'])
                self.input(by.ID,'multipartFile6',self.data['营业执照照片'])
                self.input(by.ID,'multipartFile7',self.data['主流餐饮平台认证照片'])





# k=KsPage('客商企业',2)
# k.main()










