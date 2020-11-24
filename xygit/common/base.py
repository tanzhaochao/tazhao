from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Firefox()
# driver.get("http://bj.ganji.com/")
import time
class Base():


        def __init__(self,driver):
            self.timeout = 10
            self.t = 0.5
            self.driver = driver

        def findElementNew(self,lo):
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(lo))

            return ele

        def findElementNews(self,lo):

            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(lo))

            return ele
        def findElement(self,loca):
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_element(*loca))
            return ele
        def click(self,lo):
            ele = self.findElementNew(lo)
            ele.click()

        def isSelected(self,lo):
            ele = self.findElement(lo)
            r= ele.is_selected()

            return r
        def is_title(self,title):
            try:
                ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(title))
                return ele
            except:
                return False

        def is_text_in_elemnet(self,lo1,text):
          try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(lo1,text))
                return ele
          except:
                return False

        def is_text_in_elemnet_value(self,lo1,value):
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    EC.text_to_be_present_in_element_value(lo1, value))
                return ele
            except:
                return False
        def is_alert(self):
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
                ele.accept()

            except:
                return False

        def get_text(self, locator):
           try:
                ele = self.findElementNew(locator).text
                print(ele)
                print(11111)
                return  ele
           except:
                print("获取失败")
                return False

        def senKeys(self, locator, text):
            #ele = self.findElement(locator)
            ele = self.findElementNew(locator)

            ele.clear()
            ele.send_keys(text)
            return ele
        def move_to_element(self,lo):
            '''鼠标指针移动到某个元素上 '''
            ele = self.findElementNew(lo)
            ActionChains(self.driver).move_to_element(ele).perform()

        def select_by_index(self,lo,index=0):
            ele = self.findElementNew(lo)
            Select(ele).select_by_index(index)

        def classlist(self,lo):

            #ele = self.findElementNews(lo)
            ele = driver.find_elements_by_xpath(".//*[@id='adv-setting-gpc']/div/div[2]/div[2]")
            print(type(ele))

            return ele

        def js_focus(self,lo):
            """滚动到指定位置"""
            target = self.findElementNew(lo)
            driver.execute_script("arguments[0].scrollIntoView();",target)

        def js_scroll_end(self):
            """滚动到指定底部"""
            js_heig = "window.scrollTo(0,document.body.scrollHeight)"
            driver.execute_script(js_heig)
        def js_scroll_top(self):
            """滚动到指定底部"""
            js_heig = "window.scrollTo(0,0)"
            driver.execute_script(js_heig)
if __name__=="__main__":

     aa= Base(driver)
     lo1 = (By.LINK_TEXT,"甜品")
     aa.js_focus(lo1)
     time.sleep(2)
     aa.js_scroll_end()
     time.sleep(2)
     aa.js_scroll_top()
     """ lo  =(By.ID,'s-usersetting-top')
    lo1 = (By.LINK_TEXT,"搜索设置")
    lo2 = (By.ID,"s1_1")
    lo3 = (By.ID,"s1_2")
      #aa.get_text(lo)
    #aa.move_to_element(lo)
    aa.click(lo)
    #aa.click(lo1)
    #print(aa.isSelected(lo2))
    #print(aa.isSelected(lo3))
    lo5 = (By.LINK_TEXT,"高级搜索")
    lo6 = (By.XPATH,".//*[@id='adv-setting-gpc']/div/div[2]/div[2]/p[4]")
    lo7 = (By.XPATH,".//*[@id='adv-setting-gpc']/div/div[1]/span")
    #driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[3]')
    aa.click(lo5)
    aa.click(lo7)
    print(aa.classlist(lo6)[0].text)
    aa.click(lo6)
    # print(bb[0])"""



