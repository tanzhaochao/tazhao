import unittest
from selenium import webdriver
from pages.addbug_page import AddBug
from pages.login_page import LoginPage
import time

class AddBugCase(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://39.96.26.189/")
        cls.lg = LoginPage(cls.driver)
        cls.lg.login()
        cls.ad = AddBug(cls.driver)




    def test_add_bug(self):

        self.ad.addbug()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__=="__main__":
    unittest.main()





