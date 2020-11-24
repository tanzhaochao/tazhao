from selenium import webdriver
import unittest
from pages.login_page import LoginPage,loginurl
import ddt

testdates = [
    {"usr":"1","psw":"1" ,"expect":"注销"},
    {"usr":"1","psw":" " ,"expect":False}
            ]

@ddt.ddt
class LoginCase(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(loginurl)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self,usr,psw,expect):

        self.loginp.input_usename(usr)
        self.loginp.input_password(psw)
        self.loginp.click_submit()
        self.loginp.is_alert()
        self.assertEqual(self.loginp.is_login_sucess(),expect)

    @ddt.data(*testdates)

    def test_01(self,data):
        print(data["usr"])
        self.login_case(data["usr"],data["psw"],data["expect"])








    # def test_02(self):
    #     self.loginp.input_usename(1)
    #     self.loginp.input_password(1)
    #     self.loginp.click_submit()
    #     self.loginp.is_alert()
    #     self.assertEqual(self.loginp.get_text() == False)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__== "__main__":
    unittest.main()