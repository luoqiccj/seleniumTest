#coding:utf-8
import unittest
from business.login import loginBusiness
from selenium import webdriver
from utils.get_config import getConfig
import outcome
import  sys
import os
class loginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        cfg = getConfig()
        self.driver = webdriver.Chrome()
        self.driver.get(getConfig().getconfig('url','login_url'))
        self.log_bus = loginBusiness(self.driver)

    def test_login_success(self):
        self.log_bus.login("es_superadmin","123456")

    #@unittest.skip("不执行")
    def test_login_usrname_error(self):
        res = self.log_bus.login_usrname_error("es_superadmi", "123456")
        self.assertTrue(res)

    def tearDown(self):
        print("self._testMethodName",self._testMethodName)
        self.driver.close()


if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    #suit.addTest(loginCase("test_login_success"))
    suit.addTest(loginCase("test_login_usrname_error"))
    unittest.TextTestRunner().run(suit)

