from common.base import Base
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
import random

class AddBug(Base):

    driver = webdriver.Firefox()
    def ranstr(self,num):
    # 猜猜变量名为啥叫 H
            H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

            salt = ''
            for i in range(num):
                 salt += random.choice(H)

            return salt




    def addbug(self):

        lg = LoginPage(self.driver)
        lg.login()
        lo8 = (By.XPATH,"html/body/div[1]/div[3]/div/div[2]/div[2]/input")
        self.click(lo8)
        lo1 =(By.ID,"title")
        lo2 =(By.ID,"fabu_body_neirong")
        lo3 = (By.XPATH, "html/body/div[1]/div[3]/div[4]/input")

        localtime = time.asctime(time.localtime(time.time()))
        for i in range(2):

                print(i)
                self.senKeys(lo2,("编号：%s   本次帖子内容%s本次时间%s"%(i,self.ranstr(5),localtime)))
                self.click(lo3)
                self.is_alert()
                self.click(lo8)

                # newlo = ("xpath","html/body/div[1]/div[3]/div/div[3]/div[2]/a")
                #
                # xyb.findElementNew(newlo)
                #
                # print(xyb.findElementNew(newlo).text)

        self.driver.back()

    def is_addbug_succes(self):

            newlo = (By.XPATH,"html/body/div[1]/div[3]/div/div[3]/div[2]/a")

            print(self.findElementNew(newlo).text)
            print(self.is_text_in_elemnet(newlo,"1"))
            result = self.is_text_in_elemnet(newlo,"1")
            return result


if __name__ == "__main__":
   driver = webdriver.Firefox()
   aa = AddBug(driver)
   aa.addbug()
   aa.is_addbug_succes()