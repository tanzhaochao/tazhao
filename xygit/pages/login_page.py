from  common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
loginurl = 'http://39.96.26.189/?r=user/login'
import time
class LoginPage(Base):

    username_loc = (By.ID, 'mail')
    password_loc = (By.ID, 'password')
    submit_loc = (By.XPATH,'html/body/div[1]/div[3]/div[5]/input')
    cn = (By.XPATH,'html/body/div[1]/div[2]/a[5]')

    def input_usename(self, username):
        self.senKeys(self.username_loc,username)

    def input_password(self, password):
        self.senKeys(self.password_loc,password)

    def click_submit(self):

        self.click(self.submit_loc)
    def is_login_sucess(self):

        cnn = self.get_text(self.cn)

        if cnn =="注销":
             print("登陆成功")
             return cnn

        else:
                print("登录失败")
                return False
        # try:
        #
        #     cnn =="注销"
        #     print("登陆成功")
        #     return cnn
        # except:
        #
        #     print("登录失败")
        #   return False
    def login(self,username = 1, passsword = 1 ):
        self.driver.get(loginurl)
        self.input_usename(username)
        self.input_password(passsword)
        self.click_submit()
        self.is_alert()
        # time.sleep()
        # self.driver.get("http://127.0.0.1:9001/index?do=main")
        # lo8 = (By.XPATH,"html/body/div[1]/div[3]/div/div[2]/div[2]/input")
        # self.click(lo8)
if  __name__== "__main__":

    driver = webdriver.Firefox()
    # # driver.get('http://39.96.26.189/?r=user/login')
    # #
    ll = LoginPage(driver)
    ll.login()

    # # ll.input_usename(1)
    # # ll.input_password(1)
    # # ll.click_submit()
    # ll.is_alert()
    # ll.is_login_sucess()




