# coding：utf-8
#author：jiguobin
from selenium.webdriver.common.by import By as by
from util.utils import Utils
class Public():
    def __init__(self):
        pass

    #登录ms
    def login_ms(self,type=None,url=None,name=None,password=None):
        '''
        :param url: 环境url
        :param type: 浏览器类型
        :param name: 账户
        :param password: 密码
        :return:
        '''
        if type==None:
            types='firefox'
        elif type=='c':
            types='chrome'
        self.open_browser(types)
        if url=='测试':
            test_url='http://192.168.19.103:8000/ms/login.in'
            # test_url='http://192.168.140.15/ms/login.in'
            self.get_url(test_url)
            self.input('id','logInName',name)
            self.input('id','password',password)
        elif url=='灰度':
            huidu_url='http://intms.51ebill.com/ms/login.in'
            self.get_url(huidu_url)
            self.input('id','logInName',name)
            self.input('id','password',password)
        #如果url=线上环境，账号和密码为默认
        elif url=='生产':
            online_url='http://ms.liantuobank.com/ms/login.in'
            self.get_url(online_url)
            self.input('id','logInName',name)
            self.input('id','password',password)
        #手动输入验证码
        self.sleep_time(5)
        self.click('id','submitForm')
        self.sleep_time(2)
        # while self.driver.find_element_by_id('errorVerifyCode').text=='验证码输入错误':
        #     print('输入验证码')
        #     self.sleep_time(5)
        #     self.click('id','submitForm')
        #     self.sleep_time(2)



        # try:
        #     while Utils.isElementExist(self,by.ID,'errorVerifyCode'):
        #         print('输入验证码')
        #         self.sleep_time(5)
        #         self.click('id','submitForm')
        #
        # except:
        #     self.sleep_time(2)
        # else:
        #     print('登录失败')




        #自动识别验证按
        # file_name='D:\image_code.png'
        # self.get_code_image(file_name)
        # code_text=self.code_online(file_name)
        # self.input('id','verifyCodeInput',code_text)
        # self.click('id','submitForm')
        # if self.driver.find_element_by_id('errorVerifyCode').text=='验证码输入错误':
        #     self.get_code_image(file_name)
        #     code_text=self.code_online(file_name)
        #     self.input('id','verifyCodeInput',code_text)
        #     self.click('id','submitForm')
        # self.sleep_time(2)


    #查找商户或门店进件
    def merchantType(self,type):
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        #判断是商户还是门店进件
        if self.data['商户id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[2]/a')
            self.switch_frame('contframe')
            self.input(by.ID,'searchContent',self.data['商户id'])
            self.sleep_time(0.5)
            self.click(by.ID,'searchContent')
        elif self.data['门店id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[3]/a')
            self.switch_frame('contframe')
            self.input(by.ID,'storeContent',self.data['门店id'])
            self.sleep_time(0.5)
            self.click(by.ID,'storeContent')
        else:
            print('excel取值不正确')
        self.sleep_time(2)
        self.click(by.CLASS_NAME,'item') #选中指定商户
        self.click(by.ID,'query')        #查找商户
        self.sleep_time(1)
        self.click(by.ID,'details')
        if type=='ks':
            self.click(by.ID,'addBankConfigureForKS')
        elif type=='ws':
            #下拉滚动条到底部
            js="var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            self.click(by.ID,'addBankConfigureForWS')
        elif type=='ls':
            self.click(by.ID,'addBankConfigureForYeahka')





