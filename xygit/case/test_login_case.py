from selenium import webdriver
import unittest
from pages.login_page import LoginPage,loginurl

class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(loginurl)
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_01(self):
        '''
        密码成 成功登陆
        '''
        self.loginp.input_usename(1)
        self.loginp.input_password(1)
        self.loginp.click_submit()
        self.loginp.is_alert()

        self.assertEqual(self.loginp.is_login_sucess(),"注销")

    def test_02(self):
        self.loginp.input_usename(1)
        self.loginp.input_password(5)
        self.loginp.click_submit()
        self.loginp.is_alert()
        self.assertEqual(self.loginp.is_login_sucess(),False)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__== "__main__":
    unittest.main()